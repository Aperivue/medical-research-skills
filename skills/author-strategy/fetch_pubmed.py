#!/usr/bin/env python3
"""
Fetch all PubMed publications for a given author and extract metadata.
Uses NCBI E-utilities via Biopython.

Usage:
    python fetch_pubmed.py "Author Name" [--output /path/to/output.csv] [--email user@example.com]
"""

import argparse
import csv
import re
import time
import xml.etree.ElementTree as ET
from pathlib import Path

from Bio import Entrez

BATCH_SIZE = 100


def search_pubmed(query: str) -> list[str]:
    """Search PubMed and return all PMIDs."""
    handle = Entrez.esearch(db="pubmed", term=query, retmax=0)
    record = Entrez.read(handle)
    handle.close()
    total = int(record["Count"])
    print(f"Total results: {total}")

    pmids = []
    for start in range(0, total, BATCH_SIZE):
        handle = Entrez.esearch(db="pubmed", term=query, retstart=start, retmax=BATCH_SIZE)
        record = Entrez.read(handle)
        handle.close()
        pmids.extend(record["IdList"])
        time.sleep(0.4)
    return pmids


def classify_author_position(authors: list[dict], target_last: str) -> str:
    """Determine author position: 1st, co-1st, corresponding, last, middle."""
    if not authors:
        return "unknown"

    target_idx = None
    for i, auth in enumerate(authors):
        if auth.get("LastName", "").lower() == target_last.lower():
            target_idx = i
            break

    if target_idx is None:
        for i, auth in enumerate(authors):
            if target_last.lower() in auth.get("LastName", "").lower():
                target_idx = i
                break

    if target_idx is None:
        return "unknown"

    n = len(authors)
    if target_idx == 0:
        return "1st"
    elif target_idx == n - 1:
        return "last"
    elif target_idx == 1 and n > 3:
        return "co-1st"
    elif target_idx == n - 2:
        return "co-last"
    else:
        return "middle"


def classify_study_type(title: str, abstract: str, mesh_terms: list[str], pub_types: list[str]) -> str:
    """Classify study type based on title, abstract, MeSH, and publication types."""
    text = (title + " " + abstract).lower()
    mesh_lower = " ".join(mesh_terms).lower()
    pub_lower = " ".join(pub_types).lower()

    # GBD
    if "global burden" in text or "gbd" in text:
        return "GBD"

    # SR/MA
    if ("systematic review" in text or "meta-analysis" in text or
            "systematic review" in pub_lower or "meta-analysis" in pub_lower):
        return "SR/MA"

    # National health insurance claims
    if ("national health insurance" in text or "nhis" in text or
            "claims database" in text or "nationwide cohort" in text):
        return "NHIS/Claims"

    # Cross-national / binational
    if ("cross-national" in text or "binational" in text or
            ("korea" in text and ("united states" in text or "japan" in text or
             "france" in text or "american" in text))):
        return "Cross-national"

    # National survey (KNHANES, NHANES, etc.)
    if ("knhanes" in text or "nhanes" in text or "national health and nutrition" in text or
            "kchs" in text or "national survey" in text):
        return "National survey"

    # Biobank
    if "biobank" in text:
        return "Biobank"

    # AI/ML
    if ("machine learning" in text or "deep learning" in text or
            "artificial intelligence" in text or "neural network" in text):
        return "AI/ML"

    # Clinical trial
    if "randomized" in text or "clinical trial" in pub_lower:
        return "Clinical trial"

    # Case report
    if "case report" in text or "case report" in pub_lower:
        return "Case report"

    # Letter/Commentary
    if "letter" in pub_lower or "comment" in pub_lower or "editorial" in pub_lower:
        return "Letter/Commentary"

    return "Other"


def classify_topic(title: str, abstract: str, mesh_terms: list[str]) -> str:
    """Classify topic cluster."""
    text = (title + " " + abstract).lower()

    topics = {
        "Allergy/Respiratory": ["allergy", "allergic", "asthma", "respiratory", "atopic",
                                 "rhinitis", "eczema", "copd", "pneumonia", "lung disease"],
        "Cardiovascular": ["cardiovascular", "coronary", "heart", "myocardial", "hypertension",
                          "stroke", "atherosclerosis", "arrhythmia"],
        "Mental health": ["depression", "anxiety", "mental health", "psychiatric", "suicide",
                         "adhd", "autism", "bipolar", "schizophrenia"],
        "Infectious": ["covid", "sars-cov", "infection", "vaccine", "vaccination", "herpes zoster",
                       "influenza", "hepatitis", "tuberculosis"],
        "Oncology": ["cancer", "tumor", "malignant", "neoplasm", "carcinoma", "leukemia",
                     "lymphoma"],
        "Metabolic": ["diabetes", "obesity", "metabolic", "lipid", "cholesterol", "fatty liver",
                      "bmi", "insulin"],
        "Nutrition/Lifestyle": ["diet", "nutrition", "physical activity", "exercise", "sleep",
                                "sedentary", "alcohol", "smoking"],
        "Musculoskeletal": ["osteoporosis", "fracture", "arthritis", "bone", "sarcopenia",
                           "musculoskeletal", "spine", "joint"],
        "Neurological": ["dementia", "alzheimer", "parkinson", "epilepsy", "migraine",
                        "cerebrovascular", "brain", "cognitive"],
        "Radiology/Imaging": ["radiolog", "imaging", "ct ", "mri", "ultrasound", "x-ray",
                              "mammograph", "pet", "contrast"],
        "GI/Hepatology": ["gastro", "liver", "hepat", "pancrea", "colon", "bowel",
                          "endoscop", "cirrhosis"],
        "Ophthalmology": ["ophthalm", "vision", "macular", "retinal", "eye", "glaucoma"],
        "Pediatrics": ["child", "pediatric", "adolescent", "infant", "neonatal", "prenatal",
                       "offspring"],
    }

    scores = {}
    for topic, keywords in topics.items():
        score = sum(1 for kw in keywords if kw in text)
        if score > 0:
            scores[topic] = score

    if not scores:
        return "Other"

    return max(scores, key=scores.get)


def classify_journal_tier(journal: str) -> str:
    """Classify journal into tiers."""
    j = journal.lower()

    lancet_family = ["lancet"]
    nature_family = ["nature", "nat med", "nat rev", "nat commun"]
    nejm_bmj = ["n engl j med", "bmj", "jama"]

    if any(x in j for x in lancet_family):
        return "Lancet family"
    if any(x in j for x in nature_family):
        return "Nature family"
    if any(x in j for x in nejm_bmj):
        return "NEJM/BMJ/JAMA"

    high_if = ["circulation", "eur heart j", "allergy", "j allergy clin immunol",
               "ebiomedic", "sci adv", "cell", "ann oncol", "gut", "radiology",
               "eur radiol", "invest radiol"]
    if any(x in j for x in high_if):
        return "IF>=10"

    return "Other"


def parse_article(article, target_last: str) -> dict:
    """Parse a single PubmedArticle XML element."""
    medline = article.find(".//MedlineCitation")
    art = medline.find(".//Article") if medline is not None else None

    pmid = ""
    pmid_el = medline.find(".//PMID") if medline is not None else None
    if pmid_el is not None:
        pmid = pmid_el.text or ""

    title = ""
    title_el = art.find(".//ArticleTitle") if art is not None else None
    if title_el is not None:
        title = "".join(title_el.itertext()).strip()

    journal = ""
    journal_el = art.find(".//Journal/Title") if art is not None else None
    if journal_el is not None:
        journal = journal_el.text or ""

    journal_abbrev = ""
    ja_el = art.find(".//Journal/ISOAbbreviation") if art is not None else None
    if ja_el is not None:
        journal_abbrev = ja_el.text or ""

    year = ""
    year_el = art.find(".//Journal/JournalIssue/PubDate/Year") if art is not None else None
    if year_el is not None:
        year = year_el.text or ""
    else:
        medline_date = art.find(".//Journal/JournalIssue/PubDate/MedlineDate") if art is not None else None
        if medline_date is not None and medline_date.text:
            match = re.search(r"(20\d{2}|19\d{2})", medline_date.text)
            if match:
                year = match.group(1)

    authors = []
    author_list = art.find(".//AuthorList") if art is not None else None
    if author_list is not None:
        for auth_el in author_list.findall("Author"):
            last = auth_el.find("LastName")
            fore = auth_el.find("ForeName")
            initials = auth_el.find("Initials")
            collective = auth_el.find("CollectiveName")
            auth_dict = {
                "LastName": last.text if last is not None else "",
                "ForeName": fore.text if fore is not None else "",
                "Initials": initials.text if initials is not None else "",
                "CollectiveName": collective.text if collective is not None else "",
            }
            authors.append(auth_dict)

    n_authors = len(authors)
    author_position = classify_author_position(authors, target_last)

    abstract = ""
    abstract_el = art.find(".//Abstract") if art is not None else None
    if abstract_el is not None:
        parts = []
        for at in abstract_el.findall("AbstractText"):
            parts.append("".join(at.itertext()).strip())
        abstract = " ".join(parts)

    mesh_terms = []
    mesh_list = medline.find(".//MeshHeadingList") if medline is not None else None
    if mesh_list is not None:
        for mh in mesh_list.findall("MeshHeading"):
            desc = mh.find("DescriptorName")
            if desc is not None:
                mesh_terms.append(desc.text or "")

    pub_types = []
    pt_list = art.find(".//PublicationTypeList") if art is not None else None
    if pt_list is not None:
        for pt in pt_list.findall("PublicationType"):
            pub_types.append(pt.text or "")

    study_type = classify_study_type(title, abstract, mesh_terms, pub_types)
    topic = classify_topic(title, abstract, mesh_terms)
    journal_tier = classify_journal_tier(journal_abbrev or journal)

    return {
        "pmid": pmid,
        "title": title,
        "journal": journal,
        "journal_abbrev": journal_abbrev,
        "year": year,
        "n_authors": n_authors,
        "author_position": author_position,
        "study_type": study_type,
        "topic": topic,
        "journal_tier": journal_tier,
        "pub_types": "; ".join(pub_types),
        "mesh_terms": "; ".join(mesh_terms),
        "abstract": abstract[:500],
    }


def fetch_details(pmids: list[str], target_last: str) -> list[dict]:
    """Fetch detailed metadata for a list of PMIDs."""
    all_records = []
    for start in range(0, len(pmids), BATCH_SIZE):
        batch = pmids[start:start + BATCH_SIZE]
        print(f"Fetching details {start+1}-{start+len(batch)} of {len(pmids)}...")
        handle = Entrez.efetch(db="pubmed", id=batch, rettype="xml", retmode="xml")
        xml_data = handle.read()
        handle.close()
        root = ET.fromstring(xml_data)
        for article in root.findall(".//PubmedArticle"):
            record = parse_article(article, target_last)
            all_records.append(record)
        time.sleep(0.5)
    return all_records


def main():
    parser = argparse.ArgumentParser(description="Fetch PubMed publications for an author")
    parser.add_argument("author", help="Author name for PubMed search (e.g., 'Kim DK')")
    parser.add_argument("--last-name", help="Last name for position classification (auto-detected if omitted)")
    parser.add_argument("--output", "-o", help="Output CSV path", default=None)
    parser.add_argument("--email", help="Email for NCBI E-utilities", default="research@example.com")
    args = parser.parse_args()

    Entrez.email = args.email

    # Build search query
    search_query = f'"{args.author}"[Author]'
    target_last = args.last_name or args.author.split()[-1]

    # Output path
    if args.output:
        output_csv = Path(args.output)
    else:
        safe_name = args.author.replace(" ", "_").replace('"', "")
        output_csv = Path(f"{safe_name}_publications.csv")

    print(f"Searching PubMed for: {search_query}")
    print(f"Target last name for position: {target_last}")
    pmids = search_pubmed(search_query)
    print(f"Found {len(pmids)} PMIDs")

    if not pmids:
        print("No results found. Check the author name format.")
        return

    records = fetch_details(pmids, target_last)
    print(f"Fetched details for {len(records)} articles")

    output_csv.parent.mkdir(parents=True, exist_ok=True)
    fieldnames = [
        "pmid", "title", "journal", "journal_abbrev", "year",
        "n_authors", "author_position", "study_type", "topic",
        "journal_tier", "pub_types", "mesh_terms", "abstract"
    ]

    with open(output_csv, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(records)

    print(f"\nSaved to {output_csv}")
    print(f"Total records: {len(records)}")

    # Quick summary
    from collections import Counter
    types = Counter(r["study_type"] for r in records)
    positions = Counter(r["author_position"] for r in records)

    print("\n=== Study Type Distribution ===")
    for k, v in types.most_common():
        print(f"  {k}: {v} ({v/len(records)*100:.1f}%)")

    print("\n=== Author Position ===")
    for k, v in positions.most_common():
        print(f"  {k}: {v} ({v/len(records)*100:.1f}%)")


if __name__ == "__main__":
    main()

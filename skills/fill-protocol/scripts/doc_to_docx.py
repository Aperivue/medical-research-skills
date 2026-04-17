#!/usr/bin/env python3
"""Convert .doc → .docx via LibreOffice headless. Preserves table/font/page layout.

Usage: python3 doc_to_docx.py <input.doc> [output_dir]
       python3 doc_to_docx.py <input.doc> <output.docx>
"""
import sys
import shutil
import subprocess
from pathlib import Path

SOFFICE_CANDIDATES = [
    "/Applications/LibreOffice.app/Contents/MacOS/soffice",
    "/usr/bin/soffice",
    "/opt/homebrew/bin/soffice",
    "soffice",
]


def find_soffice() -> str:
    for path in SOFFICE_CANDIDATES:
        if shutil.which(path) or Path(path).exists():
            return path
    raise FileNotFoundError(
        "LibreOffice (soffice) not found. Install with: brew install --cask libreoffice"
    )


def convert(input_path: Path, output: Path) -> Path:
    soffice = find_soffice()
    if output.is_dir() or not output.suffix:
        out_dir = output if output.is_dir() else output.parent
        out_dir.mkdir(parents=True, exist_ok=True)
        cmd = [
            soffice,
            "--headless",
            "--convert-to",
            "docx",
            "--outdir",
            str(out_dir),
            str(input_path),
        ]
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=120)
        if result.returncode != 0:
            raise RuntimeError(f"soffice conversion failed:\n{result.stderr}")
        produced = out_dir / (input_path.stem + ".docx")
        if not produced.exists():
            raise RuntimeError(f"Expected output not found: {produced}")
        return produced

    out_dir = output.parent
    out_dir.mkdir(parents=True, exist_ok=True)
    cmd = [
        soffice,
        "--headless",
        "--convert-to",
        "docx",
        "--outdir",
        str(out_dir),
        str(input_path),
    ]
    result = subprocess.run(cmd, capture_output=True, text=True, timeout=120)
    if result.returncode != 0:
        raise RuntimeError(f"soffice conversion failed:\n{result.stderr}")
    auto_name = out_dir / (input_path.stem + ".docx")
    if auto_name != output and auto_name.exists():
        auto_name.replace(output)
    return output


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)
    inp = Path(sys.argv[1]).expanduser().resolve()
    if not inp.exists():
        print(f"Input not found: {inp}", file=sys.stderr)
        sys.exit(2)
    if len(sys.argv) >= 3:
        out = Path(sys.argv[2]).expanduser().resolve()
    else:
        out = inp.with_suffix(".docx")
    produced = convert(inp, out)
    print(f"Converted: {produced}")


if __name__ == "__main__":
    main()

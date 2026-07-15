#!/usr/bin/env python3

from pathlib import Path
import sys

PROJECT_ROOT = Path(__file__).resolve().parent.parent

EXTRACTED_DIR = PROJECT_ROOT / "Extracted"
OUTPUT_DIR = PROJECT_ROOT / "output"


def check_folders():
    required = [
        EXTRACTED_DIR / "MAP",
        EXTRACTED_DIR / "MAT",
        EXTRACTED_DIR / "MFO",
        EXTRACTED_DIR / "PCX",
    ]

    missing = [p for p in required if not p.exists()]

    if missing:
        print("Missing folders:")
        for p in missing:
            print(" -", p)
        return False

    OUTPUT_DIR.mkdir(exist_ok=True)

    return True


def main():

    print("=" * 60)
    print("FlyingSB Map Explorer")
    print("=" * 60)

    if not check_folders():
        sys.exit(1)

    print("Project folders verified.\n")

    resource_types = {
        "MAP": "*.bin",
        "MAT": "*.bin",
        "MFO": "*.txt",
        "PCX": "*.bin",
    }

    print("Resources")

    for name, pattern in resource_types.items():
        count = len(list((EXTRACTED_DIR / name).glob(pattern)))
        print(f"  {name:4} : {count} files")

    print("\nReady.")


if __name__ == "__main__":
    main()
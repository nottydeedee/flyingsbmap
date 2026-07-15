from pcx import read_header
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parent.parent
PCX_DIR = ROOT / "Extracted" / "PCX"


def info_pcx(name):
    filename = PCX_DIR / f"{name}.bin"

    header = read_header(filename)

    print(name)
    print("-" * len(name))
    print(f"Size          : {header.width} x {header.height}")
    print(f"Manufacturer  : {header.manufacturer}")
    print(f"Version       : {header.version}")
    print(f"Encoding      : {header.encoding}")
    print(f"Bits/Pixel    : {header.bits_per_pixel}")
    print(f"Planes        : {header.planes}")
    print(f"Bytes/Line    : {header.bytes_per_line}")


def list_pcx():
    if not PCX_DIR.exists():
        print(f"PCX folder not found: {PCX_DIR}")
        return

    files = sorted(PCX_DIR.glob("*.bin"))

    print(f"Found {len(files)} PCX files\n")

    for f in files:
        print(f.name)


def main():
    if len(sys.argv) < 2:
        print("Usage:")
        print("  python src\\maptool.py list-pcx")
        print("  python src\\maptool.py info-pcx <name>")
        return

    cmd = sys.argv[1].lower()

    if cmd == "list-pcx":
        list_pcx()

    elif cmd == "info-pcx":
        if len(sys.argv) != 3:
            print("Usage:")
            print("  python src\\maptool.py info-pcx TAA0_00P")
            return

        info_pcx(sys.argv[2])

    else:
        print(f"Unknown command: {cmd}")


if __name__ == "__main__":
    main()
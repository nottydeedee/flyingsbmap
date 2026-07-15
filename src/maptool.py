from pathlib import Path
import sys

from pcx import read_header, export_png

ROOT = Path(__file__).resolve().parent.parent
PCX_DIR = ROOT / "Extracted" / "PCX"
OUTPUT_DIR = ROOT / "output" / "png"


def list_pcx():
    files = sorted(PCX_DIR.glob("*.bin"))

    print(f"Found {len(files)} PCX files\n")

    for f in files:
        print(f.name)


def info_pcx(name):
    filename = PCX_DIR / f"{name}.bin"

    if not filename.exists():
        print(f"File not found: {filename}")
        return

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


def export_pcx(name):
    source = PCX_DIR / f"{name}.bin"

    if not source.exists():
        print(f"File not found: {source}")
        return

    destination = OUTPUT_DIR / f"{name}.png"

    export_png(source, destination)

    print("Export complete:")
    print(destination)


def main():
    if len(sys.argv) < 2:
        print("Usage:")
        print("  python src\\maptool.py list-pcx")
        print("  python src\\maptool.py info-pcx <name>")
        print("  python src\\maptool.py export-pcx <name>")
        return

    cmd = sys.argv[1].lower()

    if cmd == "list-pcx":
        list_pcx()

    elif cmd == "info-pcx":
        if len(sys.argv) != 3:
            print("Usage: python src\\maptool.py info-pcx TAA0_00P")
            return

        info_pcx(sys.argv[2])

    elif cmd == "export-pcx":
        if len(sys.argv) != 3:
            print("Usage: python src\\maptool.py export-pcx TAA0_00P")
            return

        export_pcx(sys.argv[2])

    else:
        print(f"Unknown command: {cmd}")


if __name__ == "__main__":
    main()
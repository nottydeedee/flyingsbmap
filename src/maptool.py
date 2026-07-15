from pathlib import Path
import sys

from pcx import read_header, export_png

from map import MapFile

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


def info_map(name):
    filename = ROOT / "Extracted" / "MAP" / f"{name}.bin"

    if not filename.exists():
        print(f"File not found: {filename}")
        return

    m = MapFile(filename)

    print(name)
    print("-" * len(name))
    print(f"File size    : {m.size} bytes")
    print(f"Records      : {m.record_count}")
    print()

    print("All records:")
    print()

    m.dump_all()


def inspect_map(name):
    filename = ROOT / "Extracted" / "MAP" / f"{name}.bin"

    if not filename.exists():
        print(f"File not found: {filename}")
        return

    m = MapFile(filename)
    r = m.record(0)

    print(name)
    print("=" * len(name))
    print("Header")
    print("------")
    print(f"Field 0 : {r[0]}")
    print(f"Field 1 : {r[1]}")
    print(f"Field 2 : {r[2]}")
    print(f"Field 3 : {r[3]}")
    print(f"Field 4 : {r[4]}")
    print(f"Field 5 : {r[5]}")
    print(f"Field 6 : {r[6]}")
    print(f"Field 7 : {r[7]}")
    print(f"Field 8 : {r[8]}")
    print(f"Field 9 : {r[9]}")
    print()
    print(f"Records : {m.record_count}")


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
        print("  python src\\maptool.py inspect-map <name>")
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

    elif cmd == "info-map":
        if len(sys.argv) != 3:
            print("Usage: python src\\maptool.py info-map TAA0_00P")
            print("  python src\\maptool.py info-map <name>")
            return

        info_map(sys.argv[2])

    elif cmd == "inspect-map":
        if len(sys.argv) != 3:
            print("Usage: python src\\maptool.py inspect-map TAA0_00P")
            return

        inspect_map(sys.argv[2])

    else:
        print(f"Unknown command: {cmd}")


if __name__ == "__main__":
    main()
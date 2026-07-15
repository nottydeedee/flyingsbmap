from pathlib import Path

from map import MapFile

ROOT = Path(__file__).resolve().parent.parent
MAP_DIR = ROOT / "Extracted" / "MAP"


def decode_record(map_name, index):
    filename = MAP_DIR / f"{map_name}.bin"

    if not filename.exists():
        print(f"File not found: {filename}")
        return

    m = MapFile(filename)

    try:
        r = m.record(index)
    except IndexError:
        print(f"Record {index} does not exist.")
        return

    print(f"\n{map_name} Record {index}")
    print("=" * 40)
    print(f"Offset : 0x{r.offset:08X}")
    print()

    for i, value in enumerate(r.fields):
        print(f"Field {i:2}: {value:10}   0x{value:08X}")
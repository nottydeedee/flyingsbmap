from pathlib import Path

from map import MapFile


def inspect_file(filename, record_index):
    filename = Path(filename)

    if not filename.exists():
        print(f"File not found: {filename}")
        return

    m = MapFile(filename)

    if record_index < 0 or record_index >= m.record_count:
        print("Invalid record index.")
        return

    r = m.record(record_index)

    print(f"\n{filename.name} - Record {record_index}")
    print("=" * 40)
    print(f"Offset : 0x{r.offset:08X}\n")

    for i, value in enumerate(r.fields):
        print(f"{i:2}: {value:10} (0x{value:08X})")
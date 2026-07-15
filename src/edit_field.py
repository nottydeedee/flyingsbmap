from pathlib import Path
import struct

from map import MapFile


def edit_field(filename, record_index, field_index, new_value):
    filename = Path(filename)

    if not filename.exists():
        print(f"File not found: {filename}")
        return

    m = MapFile(filename)

    if record_index < 0 or record_index >= m.record_count:
        print("Invalid record index.")
        return

    if field_index < 0 or field_index >= 12:
        print("Field index must be between 0 and 11.")
        return

    data = bytearray(m.data)

    offset = record_index * MapFile.RECORD_SIZE + field_index * 4

    old_value = struct.unpack_from("<I", data, offset)[0]

    struct.pack_into("<I", data, offset, new_value)

    filename.write_bytes(data)

    print(f"Edited {filename}")
    print(f"Record : {record_index}")
    print(f"Field  : {field_index}")
    print(f"Old    : {old_value}")
    print(f"New    : {new_value}")
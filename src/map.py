from pathlib import Path
import struct


class MapFile:
    RECORD_SIZE = 48

    def __init__(self, filename):
        self.filename = Path(filename)
        self.data = self.filename.read_bytes()

    @property
    def size(self):
        return len(self.data)

    @property
    def record_count(self):
        return len(self.data) // self.RECORD_SIZE

    def record(self, index):
        if index < 0 or index >= self.record_count:
            raise IndexError("Record index out of range")

        offset = index * self.RECORD_SIZE

        values = struct.unpack_from("<12I", self.data, offset)

        return {
            "index": index,
            "offset": offset,
            "fields": values,
        }

    def dump_all(self):
        for index in range(self.record_count):
            print(f"Record {index}")
            print("-" * 20)

            r = self.record(index)

            for i, value in enumerate(r):
                print(f"{i:2}: {value} (0x{value:08X})")

            print()
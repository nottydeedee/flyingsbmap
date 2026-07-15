from pathlib import Path
import struct


class MapFile:
    def __init__(self, filename):
        self.filename = Path(filename)
        self.data = self.filename.read_bytes()

    @property
    def size(self):
        return len(self.data)

    @property
    def record_count(self):
        # Each map record is 48 bytes
        return self.size // 48

    def first_records(self, count=5):
        records = []

        for i in range(min(count, self.record_count)):
            offset = i * 48

            values = struct.unpack_from("<12I", self.data, offset)

            records.append(values)

        return records
from pathlib import Path
import struct


class MapRecord:
    def __init__(self, index, offset, fields):
        self.index = index
        self.offset = offset
        self.fields = tuple(fields)

    @property
    def signature(self):
        return self.fields[:4]

    @property
    def type(self):
        return self.fields[0]

    @property
    def subtype(self):
        return self.fields[1]

    @property
    def width(self):
        return self.fields[8]

    @property
    def height(self):
        return self.fields[9]

    @property
    def ref1(self):
        return self.fields[10]

    @property
    def ref2(self):
        return self.fields[11]

    def __getitem__(self, index):
        return self.fields[index]


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

        fields = struct.unpack_from("<12I", self.data, offset)

        return MapRecord(index, offset, fields)

    def records(self):
        for i in range(self.record_count):
            yield self.record(i)
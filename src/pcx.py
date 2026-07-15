from dataclasses import dataclass
from pathlib import Path
import struct


@dataclass
class PCXHeader:
    manufacturer: int
    version: int
    encoding: int
    bits_per_pixel: int
    xmin: int
    ymin: int
    xmax: int
    ymax: int
    planes: int
    bytes_per_line: int

    @property
    def width(self):
        return self.xmax - self.xmin + 1

    @property
    def height(self):
        return self.ymax - self.ymin + 1


def read_header(filename):
    filename = Path(filename)

    with filename.open("rb") as f:
        data = f.read(128)

    if len(data) != 128:
        raise ValueError("Invalid PCX header")

    return PCXHeader(
        manufacturer=data[0],
        version=data[1],
        encoding=data[2],
        bits_per_pixel=data[3],
        xmin=struct.unpack_from("<H", data, 4)[0],
        ymin=struct.unpack_from("<H", data, 6)[0],
        xmax=struct.unpack_from("<H", data, 8)[0],
        ymax=struct.unpack_from("<H", data, 10)[0],
        planes=data[65],
        bytes_per_line=struct.unpack_from("<H", data, 66)[0],
    )
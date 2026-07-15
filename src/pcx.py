from dataclasses import dataclass
from pathlib import Path
import struct

from PIL import Image


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


def export_png(source_file, output_file):
    """
    Export a PCX resource to PNG.
    """
    source_file = Path(source_file)
    output_file = Path(output_file)

    output_file.parent.mkdir(parents=True, exist_ok=True)

    with Image.open(source_file) as img:
        img.save(output_file, "PNG")

    return output_file
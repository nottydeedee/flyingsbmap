"""
PCX support for FlyingSB Map Explorer.

(Currently only validates the PCX header.
Decoding will be added next.)
"""

from pathlib import Path


class PCXHeaderError(Exception):
    """Raised when a PCX header is invalid."""


def read_header(filename):
    """
    Read and validate the 128-byte PCX header.

    Returns a dictionary describing the image.
    """

    data = Path(filename).read_bytes()

    if len(data) < 128:
        raise PCXHeaderError("File is smaller than a PCX header.")

    h = data[:128]

    if h[0] != 0x0A:
        raise PCXHeaderError("Invalid PCX manufacturer byte.")

    return {
        "manufacturer": h[0],
        "version": h[1],
        "encoding": h[2],
        "bits_per_pixel": h[3],
        "xmin": int.from_bytes(h[4:6], "little"),
        "ymin": int.from_bytes(h[6:8], "little"),
        "xmax": int.from_bytes(h[8:10], "little"),
        "ymax": int.from_bytes(h[10:12], "little"),
        "planes": h[65],
        "bytes_per_line": int.from_bytes(h[66:68], "little"),
    }
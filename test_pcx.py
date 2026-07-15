from pathlib import Path

from src.pcx import read_header

pcx_dir = Path("Extracted/PCX")

first_file = sorted(pcx_dir.glob("*.bin"))[0]

print(first_file.name)

header = read_header(first_file)

for k, v in header.items():
    print(f"{k:16} : {v}")
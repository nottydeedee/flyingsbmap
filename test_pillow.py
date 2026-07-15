from PIL import Image
from pathlib import Path

filename = Path("Extracted/PCX/TAA0_00P.bin")

try:
    img = Image.open(filename)

    print("Opened successfully!")
    print("Format:", img.format)
    print("Size:", img.size)
    print("Mode:", img.mode)

except Exception as e:
    print("Failed!")
    print(type(e).__name__)
    print(e)
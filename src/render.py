from pathlib import Path
from PIL import Image

from map import MapFile


def render_map(map_filename, pcx_filename, output_filename):
    from PIL import ImageDraw

    m = MapFile(map_filename)

    image = Image.open(pcx_filename).convert("RGB")
    draw = ImageDraw.Draw(image)

    print(f"Loaded {m.record_count} records")

    for record in m.records():

        if record.signature != (2, 15, 5, 9):
            continue

        print(record.index, record.fields)

    output_filename.parent.mkdir(parents=True, exist_ok=True)
    image.save(output_filename)

    print(f"Saved {output_filename}")
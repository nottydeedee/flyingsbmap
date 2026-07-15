from pathlib import Path
from PIL import Image

from map import MapFile


def render_map(map_filename, pcx_filename, output_filename):
    """
    Temporary renderer.

    Loads the MAP and PCX files and simply exports the PCX image.
    This verifies that our rendering pipeline works before we begin
    interpreting MAP records.
    """

    # Load map (currently unused except to verify it opens)
    m = MapFile(map_filename)

    print(f"Loaded MAP: {m.record_count} records")

    # Load PCX
    image = Image.open(pcx_filename)

    # Ensure output folder exists
    output_filename.parent.mkdir(parents=True, exist_ok=True)

    # Save a copy
    image.save(output_filename)

    print(f"Saved {output_filename}")
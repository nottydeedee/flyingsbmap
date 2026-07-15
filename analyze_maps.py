from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parent

# Allow importing from src/
sys.path.insert(0, str(ROOT / "src"))

from map import MapFile

MAP_DIR = ROOT / "Extracted" / "MAP"

for f in sorted(MAP_DIR.glob("*.bin")):
    m = MapFile(f)

    r0 = m.record(0)

    print(
        f"{f.stem:12} "
        f"records={m.record_count:4} "
        f"r0={m.record(0)}"
    )
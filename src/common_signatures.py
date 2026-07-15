from collections import Counter
from pathlib import Path

from map import MapFile


def common_signatures(map_dir):
    totals = Counter()

    maps = list(Path(map_dir).glob("*.bin"))

    for filename in maps:
        try:
            m = MapFile(filename)

            seen = set()

            for r in m.records():
                seen.add(r.signature)

            for sig in seen:
                totals[sig] += 1

        except Exception:
            pass

    print(f"Scanned {len(maps)} maps\n")

    for sig, count in totals.most_common():
        print(f"{count:4} maps : {sig}")
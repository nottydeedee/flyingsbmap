from collections import defaultdict, Counter
from pathlib import Path

from map import MapFile


def analyze_fields(map_dir, signature):
    values = defaultdict(set)
    counters = [Counter() for _ in range(12)]

    for filename in Path(map_dir).glob("*.bin"):
        try:
            m = MapFile(filename)

            for record in m.records():
                if record.signature == signature:
                    for i, value in enumerate(record.fields):
                        values[i].add(value)
                        counters[i][value] += 1

        except Exception:
            pass

    print(f"Signature {signature}\n")

    for field in range(12):
        vals = sorted(values[field])

        print(f"Field {field}")
        print(f"Unique values: {len(vals)}")

        if len(vals) <= 20:
            for value in vals:
                print(f"{value:5} : {counters[field][value]}")

        print()
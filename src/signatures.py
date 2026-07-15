from collections import defaultdict
from map import MapFile


def signature_report(filename):
    m = MapFile(filename)

    groups = defaultdict(list)

    for record in m.records():
        groups[record.signature].append(record.index)

    for sig in sorted(groups):
        indices = groups[sig]

        print(f"{sig}")
        print(f"  Count : {len(indices)}")
        print(f"  Records : {indices}")
        print()
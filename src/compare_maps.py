from collections import Counter
from map import MapFile


def compare_maps(file1, file2):
    m1 = MapFile(file1)
    m2 = MapFile(file2)

    s1 = Counter(r.signature for r in m1.records())
    s2 = Counter(r.signature for r in m2.records())

    signatures = sorted(set(s1) | set(s2))

    print(f"{'Signature':40} {'Map1':>5} {'Map2':>5}")
    print("-" * 55)

    for sig in signatures:
        print(f"{str(sig):40} {s1[sig]:5} {s2[sig]:5}")
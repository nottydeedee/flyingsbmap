from collections import Counter
from map import MapFile


def classify_map(filename):
    m = MapFile(filename)
    counts = Counter()

    for record in m.records():
        counts[record.signature] += 1

    return counts


def find_records(filename, signature):
    m = MapFile(filename)

    results = []

    for record in m.records():
        if record.signature == signature:
            results.append(record)

    return results


def field_statistics(filename):
    m = MapFile(filename)

    stats = [set() for _ in range(12)]

    for record in m.records():
        for i, value in enumerate(record.fields):
            stats[i].add(value)

    return stats
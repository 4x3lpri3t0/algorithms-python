import collections
from typing import Iterator, List


def examine_buildings_with_sunset(sequence: Iterator[int]) -> List[int]:
    BuildingWithHeight = collections.namedtuple("BuildingWithHeight", ("id", "height"))

    candidates: List[BuildingWithHeight] = []
    for building_idx, building_height in enumerate(sequence):
        while candidates and building_height >= candidates[-1].height:
            candidates.pop()
        candidates.append(BuildingWithHeight(building_idx, building_height))
    return [c.id for c in reversed(candidates)]


# TODO: Validate & Review. I think this could be achieved just by storing the max height so far and comparing each building's height against it, instead of using a stack?

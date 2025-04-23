from typing import TypedDict

from haversine import Unit, haversine


class Location(TypedDict):
    latitude: float
    longitude: float


def haversine_distance(
    location_1: Location,
    location_2: Location,
) -> float:
    return haversine(
        (location_1["latitude"], location_1["longitude"]),
        (location_2["latitude"], location_2["longitude"]),
        unit=Unit.KILOMETERS,
    )

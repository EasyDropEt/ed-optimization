from typing import TypedDict

from haversine import Unit, haversine


class Location(TypedDict):
    latitude: float
    longitude: float


def haversine_distance(
    locaction_1: Location,
    location_2: Location,
) -> float:
    return haversine(
        (locaction_1["latitude"], locaction_1["longitude"]),
        (location_2["latitude"], location_2["longitude"]),
        unit=Unit.KILOMETERS,
    )

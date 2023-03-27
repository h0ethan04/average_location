import typing
from typing import Iterable
import math

def _calculate_equirectangular_distance(center: tuple[int|float, int|float],
                        point: tuple[int|float, int|float]) -> int|float:
    ''' calculates the equirectangular distance between two objects'''
    lat1, long1 = center
    lat2, long2 = point
    dlat = math.radians(math.fabs(lat1 - lat2))
    dlong = math.radians(math.fabs(long1 - long2))
    earth_radius = 3958.8
    avglat = (lat1 + lat2) * 0.5
    x = dlong * math.cos(math.radians(avglat))
    d = math.sqrt(x**2 + dlat**2) * earth_radius
    return d


def calculate_distance(center, points: Iterable) -> Iterable[float]:
    """ calculates the average distance between all of the values"""
    for point in points:
        yield _calculate_equirectangular_distance(center, point)


def calculate_coordinates(center, bearing, distance) -> tuple[int|float, int|float]:
    """ calculates a coordinate value based on a central point,
        bearing and direction"""
    lat1, long1 = math.radians(center[0]), math.radians(center[1])
    a = math.radians(bearing)
    earth_radius = 3958.8
    lat2 = math.asin(math.sin(lat1) * math.cos(distance/earth_radius)
                     + math.cos(lat1) * math.sin(distance/earth_radius) * math.cos(a))
    long2 = long1 + math.atan2(math.sin(a) * math.sin(distance/earth_radius) * math.cos(lat1),
                               math.cos(distance/earth_radius) - math.sin(lat1) * math.sin(lat2))
    return math.degrees(lat2), (math.degrees(long2)+540)%360-180
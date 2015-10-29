import math


def _check_feature(feature):
    if feature['type'] != 'Feature':
        raise ValueError("Not a Feature")
    if feature['geometry']['type'] != "Point":
        raise ValueError("Not a Point Feature")


def distance(a, b, units="mi"):
    """Great-circle distance between two long-lat coordinates."""
    r = 3963  # radius of Earth in miles, TODO other units
    lon1, lat1 = math.radians(a[0]), math.radians(a[1])
    lon2, lat2 = math.radians(b[0]), math.radians(b[1])
    return math.acos(math.sin(lat1) * math.sin(lat2) +
                     math.cos(lat1) * math.cos(lat2) * math.cos(lon1 - lon2)) * r


def profile(features, property_name):
    xs = []
    ys = []
    x = 0
    last_point = None

    for feature in features:
        _check_feature(feature)

        y = feature['properties'][property_name]

        current_point = feature['geometry']['coordinates']
        if last_point:
            geodesic_dist = distance(current_point, last_point)
            x += geodesic_dist

        xs.append(x)
        ys.append(y)

        last_point = current_point

    return xs, ys

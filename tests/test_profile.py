import pytest
from geodesicxy import profile

points = [{
    "type": "Feature",
    "properties": {
        "elev": 77.5},
    "geometry": {
        "type": "Point",
        "coordinates": [
            -87.337875,
            36.539156]}}, {
    "type": "Feature",
    "properties": {
        "elev": 88.5},
    "geometry": {
        "type": "Point",
        "coordinates": [
            -86.577791,
            36.722137
            ]}}, {
    "type": "Feature",
    "properties": {
        "elev": 99.5},
    "geometry": {
        "type": "Point",
        "coordinates": [
            -88.247685,
            36.922175]}}]


def test_profile():
    res = profile(points, "elev")
    assert [int(x) for x in res[0]] == [0, 44, 137]  # starting point is distance of zero
    assert res[1] == [77.5, 88.5, 99.5]  # Ys


def test_bad():
    from copy import deepcopy
    bad = deepcopy(points)
    bad[0]['geometry']['type'] = "Foo"
    with pytest.raises(ValueError):
        profile(bad, "elev")
    bad = deepcopy(points)
    bad[0]['type'] = "Foo"
    with pytest.raises(ValueError):
        profile(bad, "elev")

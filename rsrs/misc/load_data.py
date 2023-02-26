import json


def load_geojson(path):
    with open(path) as f:
        src = json.load(f)
        src = src["features"]
    return src

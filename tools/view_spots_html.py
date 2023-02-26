#!/usr/bin/env python
# coding: utf-8

import os

import leafmap.foliumap as leafmap

from rsrs.misc.load_data import convert_geojson_properties


def main():
    raw_geojson = "data/P35-18_GML/P35-18_Roadside_Station.geojson"
    converted_geojson = "data/P35-18_GML/P35-18_Roadside_Station_converted.geojson"

    if not os.path.exists(converted_geojson):
        convert_geojson_properties(raw_geojson, converted_geojson)

    m = leafmap.Map(center=(37, 137), zoom=5)
    m.add_geojson(converted_geojson, layer_name="Roadside Stations")
    m.to_html("./mymap.html")


if __name__ == "__main__":
    main()

#!/usr/bin/env python
# coding: utf-8

import os
from pprint import pprint

import leafmap.foliumap as leafmap

from rsrs.common.code import get_code
from rsrs.misc.load_data import convert_geojson_properties, load_geojson


def main():
    raw_geojson = "data/P35-18_GML/P35-18_Roadside_Station.geojson"
    converted_geojson = "data/P35-18_GML/P35-18_Roadside_Station_converted.geojson"

    if not os.path.exists(converted_geojson):
        convert_geojson_properties(raw_geojson, converted_geojson)
    # json_data = load_geojson(converted_geojson)["features"]
    # pprint(json_data[0])

    m = leafmap.Map(center=(37, 137), zoom=5)
    m.add_geojson(converted_geojson, layer_name="Roadside Stations")
    m.to_html("./mymap.html")

    # PREFECTURES_JP_CODE
    # PREFECTURES_EN_CODE
    # REGION_JP_CODE
    # REGION_JP_CONTENTS
    # NAGANO_SPLIT_10
    # NAGANO_SPLIT_3
    print(get_code(["PREFECTURES_JP_CODE"])[0])


if __name__ == "__main__":
    main()

#!/usr/bin/env python
# coding: utf-8

import os
from pprint import pprint

import leafmap.foliumap as leafmap
import streamlit as st

from rsrs.common.code import get_code
from rsrs.common.properties import get_region
from rsrs.misc.load_data import convert_geojson_properties, load_geojson
from rsrs.utils.dict import get_key_from_list_in_value


def check_region(json_data):
    for station in json_data:
        properties = station["properties"]
        prefecture = properties["都道府県名"]
        municipality = properties["市町村名"]
        print(get_region(prefecture, municipality))


def main():
    # print(get_region("長野県", "上田市"))
    converted_geojson = "data/P35-18_GML/P35-18_Roadside_Station_converted.geojson"

    # if not os.path.exists(converted_geojson):
    #     convert_geojson_properties(raw_geojson, converted_geojson)
    json_data = load_geojson(converted_geojson)["features"]
    check_region(json_data)
    # pprint(json_data[0])


if __name__ == "__main__":
    main()

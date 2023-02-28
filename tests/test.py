#!/usr/bin/env python
# coding: utf-8

import os
from pprint import pprint

import leafmap.foliumap as leafmap
import pandas as pd
import streamlit as st

from rsrs.common.code import get_code
from rsrs.common.properties import get_property, get_region
from rsrs.misc.load_data import convert_geojson_properties, load_geojson
from rsrs.utils.dict import get_key_from_list_in_value
from rsrs.utils.str import custom_replace


def check_get_region_func(json_data):
    """Check if the name of the region can be found from prefecture and municipality."""
    municipality_notfound_list = []
    for station in json_data["features"]:
        properties = station["properties"]
        prefecture = properties["都道府県名"]
        municipality = properties["市町村名"]
        region = get_region(prefecture, municipality)
        if region is None:
            municipality_notfound_list.append(f"{prefecture} {municipality}")
    if not list(set(municipality_notfound_list)):
        print("All checked!!")
    else:
        pprint(set(municipality_notfound_list))
        print(len(set(municipality_notfound_list)))


def check_consistency_for_station_names(station_names_list_json, station_names_list_csv):
    station_names_list_json = [custom_replace(s) for s in station_names_list_json]
    station_names_list_csv = [custom_replace(s) for s in station_names_list_csv]
    diff = set(station_names_list_json) - set(station_names_list_csv)
    if diff:
        pprint(diff)
        print(f"{len(diff)} stations did not match.")
    else:
        print("All checked!!")


def main():
    converted_geojson = "data/P35-18_GML/P35-18_Roadside_Station_converted.geojson"

    # if not os.path.exists(converted_geojson):
    #     convert_geojson_properties(raw_geojson, converted_geojson)
    json_data = load_geojson(converted_geojson)
    print("check_get_region_func")
    check_get_region_func(json_data)
    df = pd.read_csv("data/list.csv", header=0, index_col=None)
    print("check_consistency_for_station_names")
    check_consistency_for_station_names(get_property(json_data, "道の駅名"), list(df["駅 名"]))


if __name__ == "__main__":
    main()

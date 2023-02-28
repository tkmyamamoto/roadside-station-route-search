#!/usr/bin/env python
# coding: utf-8

from rsrs.common.code import (
    NAGANO_SPLIT_2,
    NAGANO_SPLIT_3,
    NAGANO_SPLIT_10,
    PREFECTURES_JP_CODE,
    REGION_JP_CONTENTS,
)
from rsrs.utils.dict import get_key_from_list_in_value


def get_nagano_region_2(municipality: str):
    """Get nagano region from municipality.

    Args:
        municipality (str): City, wards, towns, villages, e.g. 中央区.

    Returns:
        nagano_region_2 (str): Region, 長野県北中部 or 長野県南部.

    Examples:
        >>> print(get_nagano_region_2("長野市"))
        >>> # 長野県北中部
    """
    nagano_region_10 = get_key_from_list_in_value(NAGANO_SPLIT_10, municipality)
    nagano_region_3 = get_key_from_list_in_value(NAGANO_SPLIT_3, nagano_region_10)
    nagano_region_2 = get_key_from_list_in_value(NAGANO_SPLIT_2, nagano_region_3)
    return nagano_region_2


def get_region(prefecture: str, municipality=None):
    """Get region from prefecture and municipality.

    Args:
        prefecture (str): Prefecture, e.g. 東京都.
        municipality (str): City, wards, towns, villages, e.g. 中央区.
            Required when Nagano Prefecture.

    Returns:
        region (str): Region, e.g. 関東地方.
    """
    assert prefecture in PREFECTURES_JP_CODE.keys()
    "invalid prefecture argument"
    if prefecture == "長野県" and municipality is None:
        raise ValueError("When prefecture is 長野県, municipality is also required.")

    if prefecture == "長野県":
        nagano_region_2 = get_nagano_region_2(municipality)
        region = get_key_from_list_in_value(REGION_JP_CONTENTS, nagano_region_2)
    else:
        region = get_key_from_list_in_value(REGION_JP_CONTENTS, prefecture)

    return region


def get_station_names_list(json_data, keys: list):
    """Get stations list with specified key.
    Args:
        src (dict): Loaded json data.
        keys (list): Query keys list, e.g. [["都道府県名", "北海道"], ["市町村名", "札幌市"]].

    Returns:
        station_names_match_list (list): List of station's that fit the criteria.
    """
    station_names_match_list = []
    for station in json_data["features"]:
        # if meet the requirements
        match = True
        for key in keys:
            if station["properties"][key[0]] != key[1]:
                match = False
                break
        if match:
            station_names_match_list.append(station["properties"]["道の駅名"])
    return station_names_match_list

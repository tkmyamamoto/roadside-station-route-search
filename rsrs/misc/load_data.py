#!/usr/bin/env python
# coding: utf-8

import json
from pathlib import Path

from rsrs.common.properties import get_region


def load_geojson(path):
    """Load geojson file.

    Args:
        path (str): Json path.

    Returns:
        src (dict): Loaded json data.
    """
    with open(path) as f:
        src = json.load(f)
    return src


def save_geojson(src, path):
    """Save geojson file.

    Args:
        src (dict): Json data to save.
        path (str): Json path.
    """
    with open(path, "w") as f:
        json.dump(src, f, indent=2, ensure_ascii=False)


def convert_geojson_properties(load_json_path: str, save_json_path: str):
    """Convert geojson properties.

    Args:
        load_json_path (str): Json path of roadside stations to read.

    Returns:
        save_json_path (str): Json path of roadside stations after changed to write.
    """
    # Stage 1
    values_from_to = {": 1.0": ': "○"', ": 2.0": ': "×"'}
    keys_from_to = {
        "P35_001": "緯度",
        "P35_002": "経度",
        "P35_003": "都道府県名",
        "P35_004": "市町村名",
        "P35_005": "行政区域コード",
        "P35_006": "道の駅名",
        "P35_007": "ホームページアドレス1",
        "P35_008": "ホームページアドレス2",
        "P35_009": "ホームページアドレス3",
        "P35_010": "ホームページアドレス4",
        "P35_011": "ATM",
        "P35_012": "ベビーベッド",
        "P35_013": "レストラン",
        "P35_014": "軽食・喫茶",
        "P35_015": "宿泊施設",
        "P35_016": "温泉施設",
        "P35_017": "キャンプ場等",
        "P35_018": "公園",
        "P35_019": "展望台",
        "P35_020": "美術館・博物館",
        "P35_021": "ガソリンスタンド",
        "P35_022": "EV充電施設",
        "P35_023": "無線LAN",
        "P35_024": "シャワー",
        "P35_025": "体験施設",
        "P35_026": "観光案内",
        "P35_027": "身障者トイレ",
        "P35_028": "ショップ",
    }

    read_path = Path(load_json_path)
    write_path = Path(save_json_path)

    content = read_path.read_text()

    for old_value in list(values_from_to.keys()):
        new_value = values_from_to[old_value]
        content = content.replace(old_value, new_value)

    for old_key in list(keys_from_to.keys()):
        new_key = keys_from_to[old_key]
        content = content.replace(old_key, new_key)

    write_path.write_text(content)

    # Stage 2
    content = load_geojson(write_path)
    for i in range(len(content["features"])):
        prefecture = content["features"][i]["properties"]["都道府県名"]
        municipality = content["features"][i]["properties"]["市町村名"]
        content["features"][i]["properties"]["地方名"] = get_region(prefecture, municipality)
        content["features"][i]["properties"]["都道府県内道の駅番号"] = 1
    save_geojson(content, write_path)

    print("Finish converting.")

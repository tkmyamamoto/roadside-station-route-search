#!/usr/bin/env python
# coding: utf-8

import json
from pathlib import Path


def load_geojson(path):
    """Change dict key.

    Args:
        path (str): Json path.

    Returns:
        src: Loaded json data.
    """
    with open(path) as f:
        src = json.load(f)
    return src


def change_dict_key(d: dict, old_key: str, new_key: str, default_value=None):
    """Change dict key.

    Args:
        d (dict): Target dict.
        old_key (str): Old key.
        new_key (str): New key.
        default_value (Any): Value to be added as a new element when a non-existent key is selected. (default=None)

    Example:
        >>> d = {'k1': 1, 'k2': 2, 'k3': 3}
        >>> change_dict_key(d, 'k1', 'k10')
        >>> print(d)
        >>> # {'k2': 2, 'k3': 3, 'k10': 1}

        >>> d = {'k1': 1, 'k2': 2, 'k3': 3}
        >>> change_dict_key(d, 'k10', 'k100')
        >>> print(d)
        >>> # {'k1': 1, 'k2': 2, 'k3': 3, 'k100': None}

        >>> d = {'k1': 1, 'k2': 2, 'k3': 3}
        >>> change_dict_key(d, 'k10', 'k100', 100)
        >>> print(d)
        >>> # {'k1': 1, 'k2': 2, 'k3': 3, 'k100': 100}
    """
    d[new_key] = d.pop(old_key, default_value)


def convert_geojson_properties(load_json_path: str, save_json_path: str):
    """Convert geojson properties

    Args:
        load_json_path (str): Json path of roadside stations to read.

    Returns:
        save_json_path (str): Json path of roadside stations after changed to write.
    """
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

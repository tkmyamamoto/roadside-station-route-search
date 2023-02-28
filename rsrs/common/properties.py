#!/usr/bin/env python
# coding: utf-8

from rsrs.common.code import (NAGANO_SPLIT_3, NAGANO_SPLIT_10, PREFECTURES_JP_CODE,
                              REGION_JP_CONTENTS,)
from rsrs.utils.dict import get_key_from_list_in_value


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
        nagano_region_10 = get_key_from_list_in_value(NAGANO_SPLIT_10, municipality)
        nagano_region_3 = get_key_from_list_in_value(NAGANO_SPLIT_3, nagano_region_10)
        region = get_key_from_list_in_value(REGION_JP_CONTENTS, nagano_region_3)
    else:
        region = get_key_from_list_in_value(REGION_JP_CONTENTS, prefecture)

    return region

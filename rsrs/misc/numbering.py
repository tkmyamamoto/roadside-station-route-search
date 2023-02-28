#!/usr/bin/env python
# coding: utf-8

import pandas as pd

from rsrs.common.code import PREFECTURES_JP_CODE


def numbering_for_stations(load_xlsx_path: str, save_csv_path: str):
    """Assign station numbers."""
    df = pd.read_excel(load_xlsx_path, header=0, index_col=None, usecols=[0, 1])

    prefectures = PREFECTURES_JP_CODE.keys()
    pref_column = list(df["県名"])
    station_num_per_pref_list = [pref_column.count(prefecture) for prefecture in prefectures]
    no_list = []
    for num in station_num_per_pref_list:
        no_list += list(range(1, num + 1))
    df["都道府県内No."] = no_list

    print(df)
    print("Done!!")
    df.to_csv(save_csv_path, index=False)


if __name__ == "__main__":
    # https://www.mlit.go.jp/road/Michi-no-Eki/file/list.xls
    load_xlsx_path = "data/list.xls"
    save_csv_path = "data/list.csv"
    numbering_for_stations(load_xlsx_path, save_csv_path)

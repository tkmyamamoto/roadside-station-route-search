#!/usr/bin/env python
# coding: utf-8

import os
from pprint import pprint

import folium
import leafmap.foliumap as leafmap
import streamlit as st

from rsrs.common.code import (
    NAGANO_SPLIT_3,
    NAGANO_SPLIT_10,
    PREFECTURES_JP_CODE,
    REGION_JP_CONTENTS,
    get_code,
)
from rsrs.common.properties import get_station_names_list
from rsrs.misc.load_data import convert_geojson_properties, load_geojson


def main():
    raw_geojson = "data/P35-18_GML/P35-18_Roadside_Station.geojson"
    converted_geojson = "data/P35-18_GML/P35-18_Roadside_Station_converted.geojson"

    if not os.path.exists(converted_geojson):
        convert_geojson_properties(raw_geojson, converted_geojson)
    json_data = load_geojson(converted_geojson)
    fields = list(json_data["features"][0]["properties"].keys())
    del fields[6:10]
    stations_cnt = len(json_data["features"])

    st.set_page_config(layout="wide")

    # Customize the sidebar
    # Logo
    st.markdown(
        """
        <style>
            [data-testid=stSidebar] [data-testid=stImage]{
                text-align: center;
                display: block;
                margin-left: auto;
                margin-right: auto;
                width: 100%;
            }
        </style>
        """,
        unsafe_allow_html=True,
    )
    logo = "resources/logo_michi_no_eki.png"
    st.sidebar.image(logo, width=100)

    # About
    markdown = """
    Web App URL: <https://template.streamlit.app>
    GitHub Repository: <https://github.com/giswqs/streamlit-multipage-template>
    """
    st.sidebar.title("About")
    st.sidebar.info(markdown)

    # Setting for map
    st.sidebar.header("Setting for Map")
    minimap_control = st.sidebar.checkbox("Show minimap")

    # Setting for searching
    st.sidebar.header("Setting for Searching")

    # Select roadside station
    st.sidebar.header("Choice of stations")

    def sel_callback(args):
        for arg in args:
            exec(f"st.session_state.{arg} = st.session_state.sel")
            # st.session_state.B = st.session_state.sel

    st.sidebar.write("### Control")
    st.sidebar.checkbox("select all", key="sel", on_change=sel_callback, args=[["A", "B"]])

    st.sidebar.write("### main")
    st.sidebar.checkbox("a", key="A")
    st.sidebar.checkbox("b", key="B")
    st.sidebar.checkbox("c", key="C")

    tabs_region = st.sidebar.tabs(REGION_JP_CONTENTS.keys())
    for tab_region, region in zip(tabs_region, REGION_JP_CONTENTS.keys()):
        with tab_region:
            tabs_pref = st.tabs(REGION_JP_CONTENTS[region])
            for tab_pref, pref in zip(tabs_pref, REGION_JP_CONTENTS[region]):
                if pref in ["長野県北中部", "長野県南部"]:
                    pref = "長野県"
                station_names_list = get_station_names_list(
                    json_data, [["都道府県名", pref], ["地方名", region]]
                )
                with tab_pref:
                    # st.write(pref)
                    st.write(station_names_list)
                    # for station_name in station_names_list:
                    #     st.checkbox(station_name)

    # html = "<h1>world</h1>"
    # st.components.v1.html(html)
    # st.components.v1.html("<center>" + html + "</center>")

    # Customize page title
    st.title("Streamlit for Geospatial Applications")
    st.markdown(
        """
        This multipage app template demonstrates various interactive web apps created using [streamlit](https://streamlit.io) and [leafmap](https://leafmap.org). It is an open-source project and you are very welcome to contribute to the [GitHub repository](https://github.com/giswqs/streamlit-multipage-template).
        """
    )
    st.header(f"{stations_cnt} 駅")
    m = leafmap.Map(center=(37, 137), zoom=5, minimap_control=minimap_control)
    tooltip = folium.GeoJsonTooltip(
        fields=["道の駅名"],
        labels=False,
        style=("background-color: white; color: #333333; font-family: arial; font-size: 20px"),
    )
    popup = folium.GeoJsonPopup(fields=fields, labels=True)
    folium.GeoJson(
        converted_geojson, name="Roadside Stations", tooltip=tooltip, popup=popup
    ).add_to(m)
    # m.add_geojson(converted_geojson, layer_name="Roadside Stations",tooltip=tooltip)
    m.to_streamlit()


if __name__ == "__main__":
    main()

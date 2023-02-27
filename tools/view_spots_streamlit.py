#!/usr/bin/env python
# coding: utf-8

import os
from pprint import pprint

import leafmap.foliumap as leafmap
import streamlit as st

from rsrs.common.code import get_code
from rsrs.misc.load_data import convert_geojson_properties, load_geojson


def main():
    raw_geojson = "data/P35-18_GML/P35-18_Roadside_Station.geojson"
    converted_geojson = "data/P35-18_GML/P35-18_Roadside_Station_converted.geojson"

    if not os.path.exists(converted_geojson):
        convert_geojson_properties(raw_geojson, converted_geojson)
    # json_data = load_geojson(converted_geojson)["features"]
    # pprint(json_data[0])

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
        """, unsafe_allow_html=True
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
    minimap_control = st.sidebar.checkbox('Show minimap')

    # Setting for searching
    st.sidebar.header("Setting for Searching")

    # Select roadside station
    st.sidebar.header("Choice of stations")

    # if agree:
    #     st.write('Great!')

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
    st.header("Instructions")
    m = leafmap.Map(center=(37, 137), zoom=5, minimap_control=minimap_control)
    m.add_geojson(converted_geojson, layer_name="Roadside Stations")
    m.to_streamlit()
    # m.to_streamlit(height=700)

    # PREFECTURES_JP_CODE
    # PREFECTURES_EN_CODE
    # REGION_JP_CODE
    # REGION_JP_CONTENTS
    # NAGANO_SPLIT_10
    # NAGANO_SPLIT_3
    # print(get_code(["PREFECTURES_JP_CODE"])[0])


if __name__ == "__main__":
    main()

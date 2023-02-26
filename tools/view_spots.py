from pprint import pprint

import leafmap.foliumap as leafmap

from rsrs.misc.load_data import convert_geojson_properties, load_geojson


def main():
    raw_geojson = "data/P35-18_GML/P35-18_Roadside_Station.geojson"
    converted_geojson = "data/P35-18_GML/P35-18_Roadside_Station_converted.geojson"
    convert_geojson_properties(raw_geojson, converted_geojson)
    # json_data = load_geojson(converted_geojson)["features"]
    # pprint(json_data[0])

    m = leafmap.Map(center=(37, 137), zoom=5)
    m.add_geojson(converted_geojson, layer_name="Roadside Stations")
    m.to_html("./mymap.html")


if __name__ == "__main__":
    main()

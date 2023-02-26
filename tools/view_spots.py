from pprint import pprint

import leafmap.foliumap as leafmap

from rsrs.misc.load_data import load_geojson


def main():
    # pprint(load_geojson("data/P35-18_GML/P35-18_Roadside_Station.geojson"))
    m = leafmap.Map(center=(37, 137), zoom=5)
    geojson = "data/P35-18_GML/P35-18_Roadside_Station.geojson"
    m.add_geojson(geojson, layer_name="Roadside Stations")
    m.to_html("./mymap.html")


if __name__ == "__main__":
    main()

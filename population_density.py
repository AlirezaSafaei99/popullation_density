# Import the libraries

import pandas as pd
import geopandas as gpd
import folium
from folium.features import GeoJsonTooltip
import branca.colormap as cm


# Open the files with the file path that we assign to the variables
population_data = pd.read_csv(r"D:\GIS & Geospatial Analysis with Python Geopandas and Folium\Projects\PopulationDensity\usa_population_2019.csv")
gpf = gpd.read_file(r"D:\GIS & Geospatial Analysis with Python Geopandas and Folium\Projects\PopulationDensity\us-states.json")


# Join the csv file and json file to have a unify data
join_data = gpf.merge(population_data, left_on = "name", right_on = "Geographic Area")


# Create a field and calculate the area of the each state
join_data["area_km2"] = join_data["geometry"].to_crs({"init": "epsg:3395"}).area/ 10**6
join_data["population_density"] = join_data["Total Resident Population"]/join_data["area_km2"]
df = join_data[['name', 'Total Resident Population', 'area_km2', 'population_density']]
df = df.copy()
df


# Create the range of the min and max population density for the legend
min_density = join_data["population_density"].min()
max_density = join_data["population_density"].max()
colormap = cm.linear.YlOrRd_09.scale(min_density, max_density)


# Create a style function in order to have a map style
def style_function(feature):
    density = feature["properties"]["population_density"]
    return {"fillColor": colormap(density),
            "color": "black",
            "weight": 1,
            "fillOpacity": 0.6   
    }

# Create the base map and add the density layer to the main map
base_map = folium.Map(location=[38.79, -106.53], zoom_start=4)
folium.GeoJson(join_data,
               style_function=style_function,
               tooltip=GeoJsonTooltip(fields=["name", "population_density"],
                                     aliases=["State:", "Population Density:"],
                                     localize=True)
).add_to(base_map)


# Create the caption add it to the map and display the map
colormap.caption = "Population Density"
colormap.add_to(base_map)
base_map.save("USA_POPULATION_DENSITY.html")
base_map
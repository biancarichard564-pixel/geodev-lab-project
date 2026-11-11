# Step 4: look inside one geometry
import geopandas as gpd

wards = gpd.read_file("data_folder/my_data/Patani ward.gpkg")
first = wards.geometry.iloc[0]
print(type(first))
print(first)
print("Valid:", first.is_valid)
print("Centroid:", first.centroid)
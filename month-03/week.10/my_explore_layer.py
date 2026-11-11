# Step 3: open a vector layer
import geopandas as gpd

print(gpd.list_layers("data_folder/my_data/Patani ward.gpkg"))

wards = gpd.read_file("data_folder/my_data/Patani ward.gpkg")

print(wards.head())
print("Rows and columns:", wards.shape)
print(wards.geom_type.value_counts())
print("CRS:", wards.crs)
print("Bounds:", wards.total_bounds)
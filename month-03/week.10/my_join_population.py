# Step 6: join population to wards, and fix what does not match
import pandas as pd
import geopandas as gpd

wards = gpd.read_file("data_folder/my_data/Patani ward.gpkg")
settlements = gpd.read_file("data_folder/processed/settlements.gpkg", layer="settlements")

# Perform spatial join between settlements and wards
joined = gpd.sjoin(settlements, wards, how="inner", predicate="within")

print("Spatial join head:")
print(joined.head())
print("Total matched settlements:", len(joined))
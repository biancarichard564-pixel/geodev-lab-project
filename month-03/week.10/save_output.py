# Step 8: save your outputs

import geopandas as gpd

wards = gpd.read_file("data_folder/processed/wards.gpkg", layer="wards")
wards.to_file("data_folder/processed/week10_outputs.gpkg", layer="wards_copy")
wards.drop(columns="geometry").to_csv("wards_table.csv", index=False)
print(gpd.list_layers("data_folder/processed/week10_outputs.gpkg"))
# Step 5: read settlement layer directly
# Note: The CSV file does not have columns named POINT_X and POINT_Y. 
# Instead, the settlement file Patani Settlemnet.gpkg is already a GeoPackage 
# inside data_folder/my_data/, so you don't even need to convert a CSV!

import geopandas as gpd

settlements = gpd.read_file("data_folder/my_data/Patani Settlemnet.gpkg")

print(settlements.head(3))
print("CRS:", settlements.crs)

settlements.to_file(
    "data_folder/processed/settlements.gpkg", layer="settlements", driver="GPKG"
)
print("Saved", len(settlements), "settlements")
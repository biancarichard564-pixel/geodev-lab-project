import geopandas as gpd

pop = gpd.read_file("data_folder/my_data/Patani ward.gpkg")

print(pop.head())
print("Shape:", pop.shape)
print("Columns:", list(pop.columns))
print(pop.dtypes)
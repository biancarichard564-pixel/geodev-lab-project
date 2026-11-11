# Step 2: filter, sort and add a column# Step 2: filter, sort and add a column
import pandas as pd
import geopandas as gpd

pop = gpd.read_file("data_folder/my_data/Patani ward.gpkg")

# Print the columns so you can see what is available
print("Available columns:", list(pop.columns))

# Use the first numeric/text column from your printed list below
# (Replace 'col_name' with an actual column name from your ward data, e.g., 'WARD_NAME')
col_name = pop.columns[0] 

ranked = pop.sort_values(col_name, ascending=False)
print(ranked.head(3))

print("Total rows:", len(pop))
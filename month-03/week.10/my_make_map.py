# Step 7: draw a map and save it
import geopandas as gpd
import matplotlib.pyplot as plt

wards = gpd.read_file("data_folder/my_data/Patani ward.gpkg")
settlements = gpd.read_file("data_folder/processed/settlements.gpkg", layer="settlements")

fig, ax = plt.subplots(figsize=(7, 8))
wards.plot(ax=ax, color="#E6F2F3", edgecolor="#037E8E")
settlements.plot(ax=ax, color="#094923", markersize=18)
ax.set_title("Patani Settlements and Wards")
ax.set_axis_off()

fig.savefig("month-03/week.10/patani_settlement_map.png", dpi=150, bbox_inches="tight")
print("Map saved")
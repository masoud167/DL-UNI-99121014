import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature

# Create a map using Cartopy with a PlateCarree projection
fig, ax = plt.subplots(figsize=(12, 8), dpi=300)

# Set the projection for the map (PlateCarree is a commonly used projection)
ax = plt.axes(projection=ccrs.PlateCarree())

ax.add_feature(cfeature.LAND, edgecolor='black', facecolor='lightgray')
ax.add_feature(cfeature.OCEAN, facecolor='lightblue')
ax.add_feature(cfeature.BORDERS, edgecolor='black')

# Set a proper extent to center the map on Asia
ax.set_extent([30, 150, 10, 80])

# Coordinates for Iran (around the center of the country)
iran_lon, iran_lat = 53.6880, 32.4279

# Highlight Iran by placing a red dot and labeling it
ax.scatter(iran_lon, iran_lat, color='red', s=200, transform=ccrs.PlateCarree(), zorder=5)  # Iran coordinates
ax.text(iran_lon + 2, iran_lat - 2, 'Iran', fontsize=12, ha='center', color='black', fontweight='bold', 
        transform=ccrs.PlateCarree(), zorder=6)

# Add title and labels
ax.set_title("Map of Asia with Iran Highlighted", fontsize=14)
ax.set_xlabel("Longitude")
ax.set_ylabel("Latitude")

# Save the output as an image
plt.savefig("asia_highlight_iran_cartopy.png", dpi=300)
plt.show()

print("Map saved as 'asia_highlight_iran_cartopy.png'")

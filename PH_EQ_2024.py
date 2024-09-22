import geopandas as gpd
import matplotlib as plt

# Load some example data

world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))

# Plot the data

world.plot()
plt.show()
# USA Population Density Map 🗺️📊

This project visualizes the population density of U.S. states on an interactive map. The map displays the density data using a color-coded legend, making it easy to identify highly populated and sparsely populated regions. It uses `geopandas` and `folium` to merge geographical data with population statistics and render the visualization.

## 🚀 Features

- **Population Density Visualization:**
  - Dynamically calculates population density based on total population and state area.
  - Uses a color gradient to represent density levels:
    - **Yellow:** Low density.
    - **Red:** High density.

- **Interactive Map:**
  - Hover over a state to view:
    - State name.
    - Population density.

- **Dynamic Legend:**
  - Automatically adjusts the legend range based on the dataset's minimum and maximum density values.

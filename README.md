# Zambia Energy Access Analysis

Zambia is a landlocked country in central Africa with a population of 21.31 million people. The country's energy mix is heavily dependent on Hydropower which has seen a lot of pressure due to effects of climate change such as the recent drought which was the worst recorded drought in the country's history. Being a developing country, Zambia is still making strides in providing adequate electricity for its citizens, a big aspect of this is reaching all corners of the country through the establishment of power infrastructure. The country, through an act of Parliament of 2003, established the Rural Electrification Authority (REA) with the sole goal to drive electricty access to underserved corners of the country. Unfortunately, this is still far from being the case, according to the REA [official website](https://www.rea.org.zm/remp/), the rural electrification access rate stands at only 8.1% overall. 

In it's Rural Electrification Master Plan (REMP), REA has focused its efforts on electrifying 1,217 Rrual Growth Centers, which are designated areas with concentrated populations and economic activity. Through this approach, REA had achieved an electrification rate of these centers of 45% as of 31st Mach, 2024! 

In this notebook we seek to explore this use case with open data and workflows powered by Github Copilot!

## Overview

This repository contains interactive Python notebooks that create comprehensive geospatial visualizations to help identify areas with potential energy access gaps in Zambia by overlaying:

1. **Population Density** - Shows where people live using WorldPop data
2. **Power Lines Network** - Maps the electrical transmission grid by voltage level
3. **Substations** - Plots locations of electrical substations

## Notebooks

### `energy_access.ipynb` (Original Analysis)
The original notebook creates a multi-layered geospatial visualization with:
- Population density data from WorldPop
- Power infrastructure data from OpenStreetMap using Overpass API
- Individual and combined visualizations with proper layering
- GIS analysis with 10km service area buffers around substations
- Different voltage levels in the transmission network

### `zambia_population_energy_map.ipynb` (Enhanced Version)
An enhanced notebook specifically designed for high-quality visualization with:
- ✅ **WorldPop Population Density**: Downloads Zambia's population density TIFF from WorldPop as base layer
- ✅ **Transmission Lines**: Uses overpy package with Overpass queries for OpenStreetMap power lines
- ✅ **Voltage-Specific Colors**: Each voltage level has unique color coding for optimal visibility
- ✅ **Substations Layer**: Black markers with **EXACT opacity=1.0** as top layer
- ✅ **Proper Layering**: WorldPop TIFF → Transmission Lines → Substations
- ✅ **Light Theme**: Optimized for light background with excellent contrast
- ✅ **Production Quality**: Enhanced styling, legends, and professional presentation

## Key Features

- Downloads and processes population density data from WorldPop
- Fetches power infrastructure data from OpenStreetMap using Overpass API
- Creates individual and combined visualizations with proper layering
- Implements GIS analysis techniques to estimate energy access coverage
- Visualizes different voltage levels in the transmission network
- **Enhanced color schemes** optimized for light theme and contrast
- **Professional styling** with comprehensive legends and documentation
- **High-resolution output** suitable for reports and presentations

## Technologies Used

- **Python Libraries**: GeoPandas, Matplotlib, Rasterio, NumPy, Overpy, Shapely, Pandas
- **Data Sources**: WorldPop, OpenStreetMap
- **Spatial Analysis**: Coordinate system transformations, buffering, geometric operations
- **Visualization**: Enhanced matplotlib styling with optimal contrast

## How to Use

1. Clone this repository
2. Install required dependencies: `pip install overpy geopandas rasterio matplotlib numpy requests shapely pandas tqdm`
3. Run either Jupyter notebook to generate visualizations:
   - `energy_access.ipynb` for the original analysis with service area buffers
   - `zambia_population_energy_map.ipynb` for the enhanced three-layer visualization
4. The notebooks will automatically download required population density data

## Output

The visualizations create integrated maps showing population density with power infrastructure overlaid. The enhanced notebook produces publication-quality maps with:
- **Base layer**: Population density from WorldPop with enhanced color schemes
- **Middle layer**: Transmission lines with voltage-specific color coding
- **Top layer**: Substations in black with full opacity for maximum visibility

![A map of Zambia shows the overlay of power infrastructure and population.](output.png "Zambia Energy Analysis Visual")

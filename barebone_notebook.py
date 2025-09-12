# Zambia Energy Access Analysis - Bare Bones Version

## Cell 1: Basic Imports
import os
import requests
import rasterio
import geopandas as gpd
import matplotlib.pyplot as plt
import numpy as np
import overpy
from shapely.geometry import Point, LineString, Polygon
import pandas as pd

## Cell 2: Basic Population Plot
def download_worldpop_zambia(year=2020, out_dir="data"):
    iso3 = "ZMB"
    fn = f"{iso3.lower()}_ppp_{year}_UNadj.tif"
    url = f"https://data.worldpop.org/GIS/Population/Global_2000_2020/{year}/{iso3}/{fn}"
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, fn)

    if not os.path.exists(out_path):
        with requests.get(url, stream=True, timeout=60) as r:
            r.raise_for_status()
            with open(out_path, "wb") as f:
                for chunk in r.iter_content(chunk_size=1<<20):
                    if chunk:
                        f.write(chunk)
    return out_path

def plot_population():
    tif_path = download_worldpop_zambia(2020)
    
    with rasterio.open(tif_path) as src:
        arr = src.read(1)  
        bounds = src.bounds
    
    fig, ax = plt.subplots(figsize=(10, 8))
    
    im = ax.imshow(arr, 
                   cmap='viridis', 
                   aspect='equal',
                   extent=[bounds.left, bounds.right, bounds.bottom, bounds.top])
    
    plt.colorbar(im, ax=ax)
    ax.set_title('Population Density of Zambia')
    plt.show()

# Execute
plot_population()

## Cell 3: Basic Power Lines Plot
def fetch_power_data():
    api = overpy.Overpass()
    query = """
    [out:json][timeout:1400];
    relation["boundary"="administrative"]["name"~"Zambia"]["admin_level"="2"] -> .admin_boundary;
    .admin_boundary map_to_area -> .searchArea;
    way["power"="line"](area.searchArea);
    out body; >; out skel qt;
    """
    return api.query(query)

def plot_power_lines():
    result = fetch_power_data()
    
    lines = []
    for way in result.ways:
        if way.tags.get('power') == 'line':
            coords = [(float(node.lon), float(node.lat)) for node in way.nodes]
            if len(coords) >= 2:
                lines.append(LineString(coords))
    
    if lines:
        gdf = gpd.GeoDataFrame(geometry=lines, crs='EPSG:4326')
        
        fig, ax = plt.subplots(figsize=(10, 8))
        gdf.plot(ax=ax, color='red', linewidth=1)
        ax.set_title('Zambia Power Lines')
        ax.set_aspect('equal')
        plt.show()

# Execute
plot_power_lines()

## Cell 4: Basic Substations Plot
def fetch_substations_data():
    api = overpy.Overpass()
    query = """
    [out:json][timeout:1400];
    relation["boundary"="administrative"]["name"~"Zambia"]["admin_level"="2"] -> .admin_boundary;
    .admin_boundary map_to_area -> .searchArea;
    node["power"="substation"](area.searchArea);
    out body;
    """
    return api.query(query)

def plot_substations():
    result = fetch_substations_data()
    
    points = []
    for node in result.nodes:
        if node.tags.get('power') == 'substation':
            points.append(Point(float(node.lon), float(node.lat)))
    
    if points:
        gdf = gpd.GeoDataFrame(geometry=points, crs='EPSG:4326')
        
        fig, ax = plt.subplots(figsize=(10, 8))
        gdf.plot(ax=ax, color='blue', markersize=50)
        ax.set_title('Zambia Substations')
        ax.set_aspect('equal')
        plt.show()

# Execute
plot_substations()

## Cell 5: Basic Combined Plot
def create_combined_plot():
    # Get population data
    tif_path = download_worldpop_zambia(2020)
    with rasterio.open(tif_path) as src:
        arr = src.read(1)  
        bounds = src.bounds
    
    # Get power lines
    power_result = fetch_power_data()
    power_lines = []
    for way in power_result.ways:
        if way.tags.get('power') == 'line':
            coords = [(float(node.lon), float(node.lat)) for node in way.nodes]
            if len(coords) >= 2:
                power_lines.append(LineString(coords))
    
    # Get substations
    substation_result = fetch_substations_data()
    substations = []
    for node in substation_result.nodes:
        if node.tags.get('power') == 'substation':
            substations.append(Point(float(node.lon), float(node.lat)))
    
    # Plot everything
    fig, ax = plt.subplots(figsize=(12, 10))
    
    # Population layer
    im = ax.imshow(arr, cmap='viridis', aspect='equal',
                   extent=[bounds.left, bounds.right, bounds.bottom, bounds.top],
                   alpha=0.7)
    
    # Power lines
    if power_lines:
        power_gdf = gpd.GeoDataFrame(geometry=power_lines, crs='EPSG:4326')
        power_gdf.plot(ax=ax, color='red', linewidth=1)
    
    # Substations
    if substations:
        substation_gdf = gpd.GeoDataFrame(geometry=substations, crs='EPSG:4326')
        substation_gdf.plot(ax=ax, color='blue', markersize=50)
    
    plt.colorbar(im, ax=ax)
    ax.set_title('Zambia Energy Infrastructure')
    ax.set_aspect('equal')
    plt.show()

# Execute
create_combined_plot()
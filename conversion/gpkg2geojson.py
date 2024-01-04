# -*- coding: utf-8 -*-
"""
Created on Thu Jan  4 14:40:01 2024

@author: YektaCanUzundemir
"""

import geopandas as gpd
import os

input_folder = "input_folder_path"  # Geopackage dosyalarının bulunduğu klasör
output_folder = "output_folder_path"  # Geojson dosyalarının kaydedileceği klasör

for filename in os.listdir(input_folder):
    if filename.endswith(".gpkg"):
        gpkg_path = os.path.join(input_folder, filename)

        # GeoPackage dosyasını oku
        gdf = gpd.read_file(gpkg_path)

        # GeoJSON formatında kaydet
        output_geojson_name = os.path.splitext(filename)[0] + ".geojson"
        output_geojson_path = os.path.join(output_folder, output_geojson_name)
        gdf.to_file(output_geojson_path, driver="GeoJSON")

print("İşlem tamamlandı.")

# -*- coding: utf-8 -*-
"""
Created on Thu Jan  4 11:08:06 2024

@author: YektaCanUzundemir
"""

import geopandas as gpd
import os

input_folder = "input_folder_path"  # GeoJSON dosyalarının bulunduğu klasör
output_folder = "output_folder_path"  # GeoPackage dosyalarının kaydedileceği klasör

for filename in os.listdir(input_folder):
    # Input klasörün içinden dosya uzantısı .geojson olan dosyaları seç
    if filename.endswith(".geojson"):
        geojson_path = os.path.join(input_folder, filename)
        
        # GeoPackage dosyasının adını oluştur (uzantıyı değiştir)
        gpkg_name = os.path.splitext(filename)[0] + ".gpkg"
        gpkg_path = os.path.join(output_folder, gpkg_name)
        gdf = gpd.read_file(geojson_path)
        gdf.to_file(gpkg_path, driver="GPKG")

# İşlem tamamlandı mesajı
print("İşlem tamamlandı.")


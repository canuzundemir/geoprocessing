# -*- coding: utf-8 -*-
"""
Created on Mon Dec 18 18:03:42 2023

@author: YektaCanUzundemir
"""
import os
import subprocess

def convert_geojson_to_mbtiles(geojson_path, mbtiles_path):
    subprocess.run([
        'tippecanoe',
        '-zg',
        '--drop-densest-as-needed',
        '--generate-ids',
        '-o', mbtiles_path,
        '-Z', '0', '-z', '22',
        geojson_path
    ])

def process_all_geojson_files(input_folder, output_folder):
    # Create output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Iterate over all files in the input folder
    for filename in os.listdir(input_folder):
        if filename.endswith(".geojson"):
            # Construct full paths for input and output files
            geojson_path = os.path.join(input_folder, filename)
            mbtiles_name = os.path.splitext(filename)[0] + ".mbtiles"
            mbtiles_path = os.path.join(output_folder, mbtiles_name)

            # Convert GeoJSON to MBTiles
            convert_geojson_to_mbtiles(geojson_path, mbtiles_path)

if __name__ == '__main__':
    input_folder = "input_folder_path"  # GeoJSON dosyalarının bulunduğu klasör
    output_folder = "output_folder_path"  # Mbtiles dosyalarının kaydedileceği klasör

    process_all_geojson_files(input_folder, output_folder)




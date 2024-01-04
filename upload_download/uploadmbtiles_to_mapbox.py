# -*- coding: utf-8 -*-
"""
Created on Wed Dec 20 14:42:03 2023

@author: YektaCanUzundemir
"""
import os
import uuid
from mapbox import Uploader

def upload_mbtiles(local_folder_path, username, access_token):
    uploader = Uploader(access_token)

    output_file_path = os.path.join(local_folder_path, "tileset_info.txt")
    with open(output_file_path, "w") as output_file:
        for file_name in os.listdir(local_folder_path):
            if file_name.endswith(".mbtiles"):
                file_path = os.path.join(local_folder_path, file_name)

                map_id = os.path.splitext(file_name)[0]

                # Upload
                with open(file_path, "rb") as file:
                    response = uploader.upload(file, f"{username}.{map_id}")

                # Check the response
                if response.status_code == 201:
                    tileset_id = response.json()["id"]
                    print(f"Yükleniyor... Tileset ID: {username}.{tileset_id}")
                    output_file.write(f"{map_id}\tmapbox://{username}.{tileset_id}\n")
                else:
                    print(f"Error: {response.status_code} - {response.text}")

    print(f"Layer isimleri ve Tileset id'leri bu konuma kaydedildi: {output_file_path}")

if __name__ == '__main__':
    # Credentials
    username = "username"
    access_token = "token"

    # .mbtiles verileri bu klasörde olmalı
    local_folder_path = r"C:\Users\YektaCanUzundemir\2023\mbtiles\mbtiles"

    upload_mbtiles(local_folder_path, username, access_token)











import boto3
import botocore

s3 = boto3.resource('s3')

# klasörün bulunduğu bucket adı ve klasör adı
bucket_name = 'bucket_name'
# example folder_name =  Turkey/2022/Zone_1/P1/Radar/03-1/
folder_name = 'folder_name'

# İndirme yapılacak yerel dizin
local_directory_path = 'local_path'

# Klasör objesi oluştur
folder_obj = s3.Object(bucket_name, folder_name)

# Klasördeki tüm dosyaları listele
objects = s3.Bucket(bucket_name).objects.filter(Prefix=folder_name)

# İndirme işlemi
for obj in objects:
    local_file_path = local_directory_path + '/' + obj.key[len(folder_name) + 1:]
    if not obj.key.endswith('/'): 
        try:
            s3.meta.client.download_file(bucket_name, obj.key, local_file_path)
            print(f"{obj.key} başarıyla indirildi.")
        except botocore.exceptions.ClientError as e:
            if e.response['Error']['Code'] == "404":
                print(f"{obj.key} bulunamadı.")
            else:
                raise
    else:
        print(f"{obj.key} bir klasördür ve indirme işlemi yapılmayacaktır.")

print("İndirme işlemi tamamlandı.")

import os
import subprocess
import time

#example_path = s3://doktar-classification/Turkey/2023/Zone_4/P1/
bucket_path = "bucket_path"
local_path = "local_path"

if not os.path.exists(local_path):
    os.makedirs(local_path)
timestamp = time.strftime('%Y%m%d_%H%M%S')
log_file = "log_file_path\download_log_{timestamp}.txt"

print("İndirme başlatılıyor...")

# Run the AWS CLI command to download the folder and its contents
command = f'aws s3 sync {bucket_path} {local_path} --no-progress --delete 2>&1'

start_time = time.time()
output = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

# Write the output to the log file
with open(log_file, 'a') as f:  # 'a' parametresi ile dosyayı ekleme modunda açıyoruz
    f.write(f'Downloading {bucket_path} to {local_path}\n\n')

    for line in output.stdout:
        line = line.decode('utf-8').strip()

        # Check if the line indicates that a file was downloaded successfully
        if 'download' in line and 'failed' not in line:
            # Extract the local path of the downloaded file from the AWS CLI output
            file_path = line.split(' ')[-1].replace(local_path, '')

            # Write a message to the log file indicating that the file was downloaded successfully
            f.write(f'Successfully downloaded {file_path}\n')

        # Check if the line indicates that a file failed to download
        elif 'download failed' in line:
            file_path = line.split(' ')[-1].replace(local_path, '')
            f.write(f'Failed to download {file_path}\n')

        f.write(line + '\n')
        print(line)

end_time = time.time()
total_time = end_time - start_time
print(f"Toplam süre: {total_time} saniye\n")
print(f"\nİndirme tamamlandı. İndirme sürecini takip etmek için dosya yolundaki {log_file} dosyasını inceleyebilirsiniz.")


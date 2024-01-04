import boto3
import os

# Set up the S3 client with your AWS credentials
s3_client = boto3.client(
    's3',
    aws_access_key_id='AKI*******',
    aws_secret_access_key='IQ**********'
)

# Define the local folder you want to upload to S3
local_folder = 'local_folder'

# Define the S3 bucket and folder where you want to upload the files
bucket_name = 'doktar-classification'
s3_folder = 'ziya-backup'

for root, dirs, files in os.walk(local_folder):
    for file in files:
        local_path = os.path.join(root, file)

        relative_path = os.path.relpath(local_path, local_folder)

        s3_path = os.path.join(s3_folder, relative_path).replace("\\", "/")

        # Upload the file to S3
        s3_client.upload_file(local_path, bucket_name, s3_path)
        print(f"{local_path} has been uploaded to {s3_path} in the {bucket_name} bucket.")

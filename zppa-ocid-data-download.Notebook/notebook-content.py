# Fabric notebook source

# METADATA ********************

# META {
# META   "kernel_info": {
# META     "name": "synapse_pyspark"
# META   },
# META   "dependencies": {}
# META }

# MARKDOWN ********************

# # Automated Download, Extraction, and Upload of Zambia Procurement Data to Azure Blob Storage


# CELL ********************

%run procurement_config_notebook

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

import requests
import zipfile
import os
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient

# Azure Blob Storage details
connect_str = connect_str_azure_blob_storage
container_name = container_name_azure_blob_storage

# Create the BlobServiceClient object
blob_service_client = BlobServiceClient.from_connection_string(connect_str)

# Base URL for the ZIP files
base_url = "https://www.zppa.org.zm/ocds/services/recordpackage/getrecordpackage"

# Loop through the years and months
for year in range(2025, 2026):
    for month in range(1, 13):
        # Create the URL without using two digits for the month
        url = f"{base_url}/{year}/{month}"
        print(f"Processing URL: {url}")

        # Check if the file at the remote location is a text file with charset UTF-8
        response = requests.head(url)
        content_type = response.headers.get('Content-Type')
        
        if content_type == 'text/plain;charset=UTF-8':
            print(f"The file at {url} is a text file. Skipping download.")
        else:
            print(f"The file at {url} is not a text file. Downloading...")
            
            # Define the local path to save the ZIP file
            local_zip_path = f'downloaded_file_{year}_{month}.zip'
            extract_path = f'extracted_files_{year}_{month}'

            # Download the ZIP file
            response = requests.get(url)
            with open(local_zip_path, 'wb') as file:
                file.write(response.content)

            # Unzip the file
            with zipfile.ZipFile(local_zip_path, 'r') as zip_ref:
                zip_ref.extractall(extract_path)

            # Upload files to Azure Blob Storage
            for root, dirs, files in os.walk(extract_path):
                for file_name in files:
                    file_path = os.path.join(root, file_name)
                    blob_client = blob_service_client.get_blob_client(container=container_name, blob=file_name)
                    
                    # Check if the blob already exists
                    if not blob_client.exists():
                        with open(file_path, 'rb') as data:
                            blob_client.upload_blob(data)
                    else:
                        print(f"File {file_name} already exists in the blob. Skipping upload.")

print("Files uploaded successfully!")


# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# Fabric notebook source

# METADATA ********************

# META {
# META   "kernel_info": {
# META     "name": "synapse_pyspark"
# META   },
# META   "dependencies": {}
# META }

# CELL ********************

# Welcome to your new notebook
# Type here in the cell editor to add code!


# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

%run procurement_config_notebook

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient

# Define your connection string and container names
connection_string = connect_str_azure_blob_storage
source_container_name = "zambiabudgetspeech"
destination_container_name = "zambianationandlocalgovernment"

# Create a BlobServiceClient
blob_service_client = BlobServiceClient.from_connection_string(connection_string)

# Get the source and destination container clients
source_container_client = blob_service_client.get_container_client(source_container_name)
destination_container_client = blob_service_client.get_container_client(destination_container_name)

# List all blobs in the source container
blobs_list = source_container_client.list_blobs()

for blob in blobs_list:
    # Get the blob client for the source blob
    source_blob_client = source_container_client.get_blob_client(blob.name)
    
    # Modify the blob name to include the source container name
    new_blob_name = f"{source_container_name}-{blob.name}"
    
    # Get the blob client for the destination blob with the new name
    destination_blob_client = destination_container_client.get_blob_client(new_blob_name)
    
    # Copy the blob from the source container to the destination container
    copy_source = source_blob_client.url
    destination_blob_client.start_copy_from_url(copy_source)

    print(f"Copied blob {blob.name} from {source_container_name} to {destination_container_name} as {new_blob_name}")

print("All blobs have been copied.")


# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

import requests
from urllib.parse import urlparse, parse_qs
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient

# Define the URL of the PDF and the Azure Blob Storage details
pdf_url = "https://www.ago.gov.zm/?wpfb_dl=315"
azure_connection_string = connect_str_azure_blob_storage
container_name = "zambianationandlocalgovernment"

# Extract the file name from the URL
parsed_url = urlparse(pdf_url)
query_params = parse_qs(parsed_url.query)
file_name = "auditorgeneralsreports-" + query_params.get('wpfb_dl', ['downloaded_file'])[0] + '.pdf'

# Download the PDF
response = requests.get(pdf_url)
pdf_content = response.content

# Create the BlobServiceClient object
blob_service_client = BlobServiceClient.from_connection_string(azure_connection_string)

# Create a container if it doesn't exist
container_client = blob_service_client.get_container_client(container_name)
try:
    container_client.create_container()
except Exception as e:
    print(f"Container already exists: {e}")

# Create a blob client using the extracted file name as the name for the blob
blob_client = blob_service_client.get_blob_client(container=container_name, blob=file_name)

# Upload the PDF to Azure Blob Storage
try:
    blob_client.upload_blob(pdf_content, overwrite=True)
    print(f"PDF uploaded to Azure Blob Storage as {file_name}")
except Exception as e:
    print(f"Failed to upload PDF: {e}")


# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# Fabric notebook source

# METADATA ********************

# META {
# META   "kernel_info": {
# META     "name": "synapse_pyspark"
# META   },
# META   "dependencies": {
# META     "lakehouse": {
# META       "default_lakehouse": "fd8fb1e9-2469-42fb-8e24-20be00f90373",
# META       "default_lakehouse_name": "LH_Procurement",
# META       "default_lakehouse_workspace_id": "65f75a74-be1e-4c56-9c2d-5c7b1f01b59c"
# META     }
# META   }
# META }

# MARKDOWN ********************

# # Processing and Inserting OCDS JSON Records from Azure Blob Storage into a Lakehouse


# CELL ********************

%run procurement_config_notebook

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

import json
import uuid
from azure.storage.blob import BlobServiceClient
from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, StringType

# Azure Blob Storage configuration
AZURE_CONNECTION_STRING = connect_str_azure_blob_storage
CONTAINER_NAME = container_name_azure_blob_storage

# Initialize the BlobServiceClient
blob_service_client = BlobServiceClient.from_connection_string(AZURE_CONNECTION_STRING)
container_client = blob_service_client.get_container_client(CONTAINER_NAME)

# Define the schema for the DataFrame
schema = StructType([
    StructField("compiledRelease", StringType(), True),
    StructField("ocid", StringType(), True),
    StructField("releases", StringType(), True),
    StructField("versionedRelease", StringType(), True),
    StructField("parentFileName", StringType(), True)
])

# Step 1: List all blobs in the container
blob_list = container_client.list_blobs()

# Step 2: Process each blob separately
for blob in blob_list:
    blob_name = blob.name
    blob_client = blob_service_client.get_blob_client(container=CONTAINER_NAME, blob=blob_name)
    
    # Download the JSON file from Azure Blob Storage
    json_data = blob_client.download_blob().readall()
    json_content = json.loads(json_data)
    print(F"Downloaded blob. {blob_name}")
    # Extract the "records" array
    records = json_content.get("records", [])
    
    # Split the records into smaller chunks
    chunk_size = 1000  # Adjust the chunk size as needed
    chunks = [records[i:i + chunk_size] for i in range(0, len(records), chunk_size)]
    
    # Process each chunk separately
    for chunk in chunks:
        # Extract the required fields and add the parentFileName
        processed_chunk = [
            {
                "compiledRelease": json.dumps(record.get("compiledRelease")),
                "ocid": record.get("ocid"),
                "releases": json.dumps(record.get("releases")),
                "versionedRelease": json.dumps(record.get("versionedRelease")),
                "parentFileName": blob_name
            }
            for record in chunk
        ]
        
        # Convert the processed chunk to a DataFrame with the defined schema
        df = spark.createDataFrame(processed_chunk, schema=schema)
        
        # Insert the DataFrame into the procurement table
        df.createOrReplaceTempView("temp_procurement")
        print("Temp table created.")
        spark.sql("""
            INSERT INTO procurement
            SELECT * FROM temp_procurement 
        """)

        # Drop the temporary view
        spark.catalog.dropTempView("temp_procurement")
        print("Temp table dropped.")

print("Records inserted into the procurement Delta table successfully.")


# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

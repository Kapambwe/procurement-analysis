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

# CELL ********************

# Welcome to your new notebook
# Type here in the cell editor to add code!


# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# Import necessary libraries
from pyspark.sql import SparkSession
from pyspark.sql.functions import from_json, col, explode
from pyspark.sql.types import *

# Define the schema
schema = StructType([
    StructField("contracts", ArrayType(StructType([
        StructField("awardID", StringType(), True),
        StructField("dateSigned", StringType(), True),
        StructField("description", StringType(), True),
        StructField("id", StringType(), True),
        StructField("items", ArrayType(StructType([
            StructField("classification", StructType([
                StructField("description", StringType(), True),
                StructField("id", StringType(), True),
                StructField("scheme", StringType(), True),
                StructField("uri", StringType(), True)
            ]), True),
            StructField("description", StringType(), True),
            StructField("id", StringType(), True)
        ])), True),
        StructField("status", StringType(), True),
        StructField("title", StringType(), True),
        StructField("value", StructType([
            StructField("amount", IntegerType(), True),
            StructField("currency", StringType(), True)
        ]), True)
    ])), True)
])

# Read the table
df = spark.sql("SELECT * FROM Lh_procurement.procurement")

# Extract the compiledRelease column and create a temporary view
df.select(from_json(col("compiledRelease"), schema).alias("compiledRelease")).createOrReplaceTempView("records_table")

# Execute the SQL query to extract the desired fields from the contracts array
contracts_df = spark.sql("""
  SELECT
    contract.awardID,
    contract.dateSigned,
    contract.description,
    contract.id,
    item.classification.description AS item_classification_description,
    item.classification.id AS item_classification_id,
    item.classification.scheme AS item_classification_scheme,
    item.classification.uri AS item_classification_uri,
    item.description AS item_description,
    item.id AS item_id,
    contract.status,
    contract.title,
    contract.value.amount AS contract_value_amount,
    contract.value.currency AS contract_value_currency
  FROM records_table c
  LATERAL VIEW explode(c.compiledRelease.contracts) exploded_contracts AS contract
  LATERAL VIEW explode(contract.items) exploded_items AS item
""")

#display(contracts_df)
# Write the DataFrame to the Delta table
contracts_df.write.format("delta").mode("overwrite").saveAsTable("ContractCompiledReleaseTable")


# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

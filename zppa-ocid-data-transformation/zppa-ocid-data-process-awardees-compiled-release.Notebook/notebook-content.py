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

# Initialize SparkSession

# Define the schema
schema = StructType([
    StructField("awards", ArrayType(StructType([
        StructField("date", StringType(), True),
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
            StructField("id", StringType(), True),
            StructField("quantity", IntegerType(), True),
            StructField("unit", StructType([
                StructField("name", StringType(), True)
            ]), True)
        ])), True),
        StructField("status", StringType(), True),
        StructField("suppliers", ArrayType(StructType([
            StructField("address", StructType([
                StructField("countryName", StringType(), True),
                StructField("locality", StringType(), True),
                StructField("postalCode", StringType(), True),
                StructField("region", StringType(), True),
                StructField("streetAddress", StringType(), True)
            ]), True),
            StructField("contactPoint", StructType([
                StructField("telephone", StringType(), True)
            ]), True),
            StructField("identifier", StructType([
                StructField("id", StringType(), True),
                StructField("legalName", StringType(), True),
                StructField("scheme", StringType(), True),
                StructField("uri", StringType(), True)
            ]), True),
            StructField("name", StringType(), True)
        ])), True),
        StructField("title", StringType(), True),
        StructField("value", StructType([
            StructField("amount", IntegerType(), True),
            StructField("currency", StringType(), True)
        ]), True)
    ])), True),
    StructField("buyer", StructType([
        StructField("name", StringType(), True)
    ]), True),
    StructField("tender", StructType([
        StructField("title", StringType(), True),
        StructField("id", StringType(), True)
    ]), True),
    StructField("date", StringType(), True),
    StructField("ocid", StringType(), True)
])

# Read the table
df = spark.sql("SELECT * FROM Lh_procurement.procurement")

# Extract the compiledRelease column and create a temporary view
df.select(from_json(col("compiledRelease"), schema).alias("compiledRelease")).createOrReplaceTempView("records_table")

# Execute the SQL query to extract the desired fields from the awards array, along with tender name and buyer name
awards_df = spark.sql("""
  SELECT
    award.date,
    award.description,
    award.id,
    item.classification.description AS item_classification_description,
    item.classification.id AS item_classification_id,
    item.classification.scheme AS item_classification_scheme,
    item.classification.uri AS item_classification_uri,
    item.description AS item_description,
    item.id AS item_id,
    item.quantity,
    item.unit.name AS item_unit_name,
    award.status,
    supplier.address.countryName AS supplier_countryName,
    supplier.address.locality AS supplier_locality,
    supplier.address.postalCode AS supplier_postalCode,
    supplier.address.region AS supplier_region,
    supplier.address.streetAddress AS supplier_streetAddress,
    supplier.contactPoint.telephone AS supplier_contact_telephone,
    supplier.identifier.id AS supplier_identifier_id,
    supplier.identifier.legalName AS supplier_legalName,
    supplier.identifier.scheme AS supplier_scheme,
    supplier.identifier.uri AS supplier_uri,
    supplier.name AS supplier_name,
    award.title,
    award.value.amount AS award_value_amount,
    award.value.currency AS award_value_currency,
    c.compiledRelease.tender.title AS tender_title,
    c.compiledRelease.tender.id AS tender_id,
    c.compiledRelease.buyer.name AS buyer_name,
    c.compiledRelease.date AS created_date,
    c.compiledRelease.ocid AS ocid
  FROM records_table c
  LATERAL VIEW explode(c.compiledRelease.awards) exploded_awards AS award
  LATERAL VIEW explode(award.items) exploded_items AS item
  LATERAL VIEW explode(award.suppliers) exploded_suppliers AS supplier
""")

#display(awards_df)
# Write the DataFrame to the Delta table
awards_df.write.format("delta").mode("overwrite").saveAsTable("AwardCompiledReleaseTablev1")

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

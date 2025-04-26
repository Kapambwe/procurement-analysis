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
spark = SparkSession.builder \
    .appName("Extract Tenderers Fields with Tender and Buyer Name") \
    .getOrCreate()

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
        StructField("address", StructType([
            StructField("countryName", StringType(), True),
            StructField("locality", StringType(), True),
            StructField("postalCode", StringType(), True),
            StructField("region", StringType(), True),
            StructField("streetAddress", StringType(), True)
        ]), True),
        StructField("contactPoint", StructType([
            StructField("email", StringType(), True),
            StructField("faxNumber", StringType(), True),
            StructField("telephone", StringType(), True)
        ]), True),
        StructField("identifier", StructType([
            StructField("legalName", StringType(), True),
            StructField("scheme", StringType(), True),
            StructField("uri", StringType(), True)
        ]), True),
        StructField("name", StringType(), True)
    ]), True),
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
    ])), True),
    StructField("date", StringType(), True),
    StructField("id", StringType(), True),
    StructField("initiationType", StringType(), True),
    StructField("language", StringType(), True),
    StructField("ocid", StringType(), True),
    StructField("planning", StructType([
        StructField("budget", StructType([
            StructField("amount", StructType([
                StructField("amount", IntegerType(), True),
                StructField("currency", StringType(), True)
            ]), True),
            StructField("description", StringType(), True),
            StructField("id", StringType(), True),
            StructField("project", StringType(), True),
            StructField("projectID", StringType(), True)
        ]), True),
        StructField("rationale", StringType(), True)
    ]), True),
    StructField("tag", ArrayType(StringType(), True), True),
    StructField("tender", StructType([
        StructField("awardCriteria", StringType(), True),
        StructField("awardCriteriaDetails", StringType(), True),
        StructField("awardPeriod", StructType([
            StructField("endDate", StringType(), True),
            StructField("startDate", StringType(), True)
        ]), True),
        StructField("description", StringType(), True),
        StructField("documents", ArrayType(StructType([
            StructField("dateModified", StringType(), True),
            StructField("datePublished", StringType(), True),
            StructField("description", StringType(), True),
            StructField("documentType", StringType(), True),
            StructField("format", StringType(), True),
            StructField("id", StringType(), True),
            StructField("language", StringType(), True),
            StructField("title", StringType(), True),
            StructField("url", StringType(), True)
        ])), True),
        StructField("eligibilityCriteria", StringType(), True),
        StructField("enquiryPeriod", StructType([
            StructField("endDate", StringType(), True),
            StructField("startDate", StringType(), True)
        ]), True),
        StructField("hasEnquiries", BooleanType(), True),
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
        StructField("numberOfTenderers", IntegerType(), True),
        StructField("procurementMethod", StringType(), True),
        StructField("procurementMethodRationale", StringType(), True),
        StructField("procuringEntity", StructType([
            StructField("address", StructType([
                StructField("countryName", StringType(), True),
                StructField("locality", StringType(), True),
                StructField("postalCode", StringType(), True),
                StructField("region", StringType(), True),
                StructField("streetAddress", StringType(), True)
            ]), True),
            StructField("contactPoint", StructType([
                StructField("email", StringType(), True),
                StructField("faxNumber", StringType(), True),
                StructField("telephone", StringType(), True)
            ]), True),
            StructField("identifier", StructType([
                StructField("legalName", StringType(), True),
                StructField("scheme", StringType(), True),
                StructField("uri", StringType(), True)
            ]), True),
            StructField("name", StringType(), True)
        ]), True),
        StructField("status", StringType(), True),
        StructField("submissionMethod", ArrayType(StringType(), True), True),
        StructField("submissionMethodDetails", StringType(), True),
        StructField("tenderers", ArrayType(StructType([
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
        StructField("tenderPeriod", StructType([
            StructField("endDate", StringType(), True),
            StructField("startDate", StringType(), True)
        ]), True),
        StructField("title", StringType(), True),
        StructField("value", StructType([
            StructField("amount", IntegerType(), True),
            StructField("currency", StringType(), True)
        ]), True)
    ]), True)
])

# Read the table
df = spark.sql("SELECT * FROM Lh_procurement.procurement WHERE parentFileName = 'recordPackage_2024_10_1.json'")

# Extract the compiledRelease column and create a temporary view
df.select(from_json(col("compiledRelease"), schema).alias("compiledRelease")).createOrReplaceTempView("records_table")

# Execute the SQL query to extract the desired fields from the tenderers array, along with tender name and buyer name
tenderers_df = spark.sql("""
  SELECT
    tenderer.address.countryName AS tenderer_countryName,
    tenderer.address.locality AS tenderer_locality,
    tenderer.address.postalCode AS tenderer_postalCode,
    tenderer.address.region AS tenderer_region,
    tenderer.address.streetAddress AS tenderer_streetAddress,
    tenderer.contactPoint.telephone AS tenderer_contact_telephone,
    tenderer.identifier.id AS tenderer_identifier_id,
    tenderer.identifier.legalName AS tenderer_legalName,
    tenderer.identifier.scheme AS tenderer_scheme,
    tenderer.identifier.uri AS tenderer_uri,
    tenderer.name AS tenderer_name,
    c.compiledRelease.tender.title AS tender_title,
    c.compiledRelease.buyer.name AS buyer_name
  FROM records_table c
  LATERAL VIEW explode(c.compiledRelease.tender.tenderers) exploded_tenderers AS tenderer
""")

# Create a temporary view for the extracted data
tenderers_df.createOrReplaceTempView("temp_compiledreleases")

# Perform the merge operation
spark.sql("""
    MERGE INTO TendererCompiledReleaseTable AS target
    USING temp_compiledreleases AS source
    ON target.tenderer_identifier_id = source.tenderer_identifier_id
    AND target.tender_title = source.tender_title
    WHEN MATCHED THEN
      UPDATE SET
        target.tenderer_countryName = source.tenderer_countryName,
        target.tenderer_locality = source.tenderer_locality,
        target.tenderer_postalCode = source.tenderer_postalCode,
        target.tenderer_region = source.tenderer_region,
        target.tenderer_streetAddress = source.tenderer_streetAddress,
        target.tenderer_contact_telephone = source.tenderer_contact_telephone,
        target.tenderer_identifier_id = source.tenderer_identifier_id,
        target.tenderer_legalName = source.tenderer_legalName,
        target.tenderer_scheme = source.tenderer_scheme,
        target.tenderer_uri = source.tenderer_uri,
        target.tenderer_name = source.tenderer_name,
        target.tender_title = source.tender_title,
        target.buyer_name = source.buyer_name
    WHEN NOT MATCHED THEN
      INSERT (
        tenderer_countryName,
        tenderer_locality,
        tenderer_postalCode,
        tenderer_region,
        tenderer_streetAddress,
        tenderer_contact_telephone,
        tenderer_identifier_id,
        tenderer_legalName,
        tenderer_scheme,
        tenderer_uri,
        tenderer_name,
        tender_title,
        buyer_name
      ) VALUES (
        source.tenderer_countryName,
        source.tenderer_locality,
        source.tenderer_postalCode,
        source.tenderer_region,
        source.tenderer_streetAddress,
        source.tenderer_contact_telephone,
        source.tenderer_identifier_id,
        source.tenderer_legalName,
        source.tenderer_scheme,
        source.tenderer_uri,
        source.tenderer_name,
        source.tender_title,
        source.buyer_name
      )
""")


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
spark = SparkSession.builder \
    .appName("Extract Tenderers Fields with Tender and Buyer Name") \
    .getOrCreate()

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
        StructField("address", StructType([
            StructField("countryName", StringType(), True),
            StructField("locality", StringType(), True),
            StructField("postalCode", StringType(), True),
            StructField("region", StringType(), True),
            StructField("streetAddress", StringType(), True)
        ]), True),
        StructField("contactPoint", StructType([
            StructField("email", StringType(), True),
            StructField("faxNumber", StringType(), True),
            StructField("telephone", StringType(), True)
        ]), True),
        StructField("identifier", StructType([
            StructField("legalName", StringType(), True),
            StructField("scheme", StringType(), True),
            StructField("uri", StringType(), True)
        ]), True),
        StructField("name", StringType(), True)
    ]), True),
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
    ])), True),
    StructField("date", StringType(), True),
    StructField("id", StringType(), True),
    StructField("initiationType", StringType(), True),
    StructField("language", StringType(), True),
    StructField("ocid", StringType(), True),
    StructField("planning", StructType([
        StructField("budget", StructType([
            StructField("amount", StructType([
                StructField("amount", IntegerType(), True),
                StructField("currency", StringType(), True)
            ]), True),
            StructField("description", StringType(), True),
            StructField("id", StringType(), True),
            StructField("project", StringType(), True),
            StructField("projectID", StringType(), True)
        ]), True),
        StructField("rationale", StringType(), True)
    ]), True),
    StructField("tag", ArrayType(StringType(), True), True),
    StructField("tender", StructType([
        StructField("awardCriteria", StringType(), True),
        StructField("awardCriteriaDetails", StringType(), True),
        StructField("awardPeriod", StructType([
            StructField("endDate", StringType(), True),
            StructField("startDate", StringType(), True)
        ]), True),
        StructField("description", StringType(), True),
        StructField("documents", ArrayType(StructType([
            StructField("dateModified", StringType(), True),
            StructField("datePublished", StringType(), True),
            StructField("description", StringType(), True),
            StructField("documentType", StringType(), True),
            StructField("format", StringType(), True),
            StructField("id", StringType(), True),
            StructField("language", StringType(), True),
            StructField("title", StringType(), True),
            StructField("url", StringType(), True)
        ])), True),
        StructField("eligibilityCriteria", StringType(), True),
        StructField("enquiryPeriod", StructType([
            StructField("endDate", StringType(), True),
            StructField("startDate", StringType(), True)
        ]), True),
        StructField("hasEnquiries", BooleanType(), True),
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
        StructField("numberOfTenderers", IntegerType(), True),
        StructField("procurementMethod", StringType(), True),
        StructField("procurementMethodRationale", StringType(), True),
        StructField("procuringEntity", StructType([
            StructField("address", StructType([
                StructField("countryName", StringType(), True),
                StructField("locality", StringType(), True),
                StructField("postalCode", StringType(), True),
                StructField("region", StringType(), True),
                StructField("streetAddress", StringType(), True)
            ]), True),
            StructField("contactPoint", StructType([
                StructField("email", StringType(), True),
                StructField("faxNumber", StringType(), True),
                StructField("telephone", StringType(), True)
            ]), True),
            StructField("identifier", StructType([
                StructField("legalName", StringType(), True),
                StructField("scheme", StringType(), True),
                StructField("uri", StringType(), True)
            ]), True),
            StructField("name", StringType(), True)
        ]), True),
        StructField("status", StringType(), True),
        StructField("submissionMethod", ArrayType(StringType(), True), True),
        StructField("submissionMethodDetails", StringType(), True),
        StructField("tenderers", ArrayType(StructType([
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
        StructField("tenderPeriod", StructType([
            StructField("endDate", StringType(), True),
            StructField("startDate", StringType(), True)
        ]), True),
        StructField("title", StringType(), True),
        StructField("value", StructType([
            StructField("amount", IntegerType(), True),
            StructField("currency", StringType(), True)
        ]), True)
    ]), True)
])

# Read the table
df = spark.sql("SELECT * FROM Lh_procurement.procurement WHERE parentFileName = 'recordPackage_2024_10_1.json'")

# Extract the compiledRelease column and create a temporary view
df.select(from_json(col("compiledRelease"), schema).alias("compiledRelease")).createOrReplaceTempView("records_table")

# Execute the SQL query to extract the desired fields from the tenderers array, along with tender name and buyer name
tenderers_df = spark.sql("""
  SELECT
    tenderer.address.countryName AS tenderer_countryName,
    tenderer.address.locality AS tenderer_locality,
    tenderer.address.postalCode AS tenderer_postalCode,
    tenderer.address.region AS tenderer_region,
    tenderer.address.streetAddress AS tenderer_streetAddress,
    tenderer.contactPoint.telephone AS tenderer_contact_telephone,
    tenderer.identifier.id AS tenderer_identifier_id,
    tenderer.identifier.legalName AS tenderer_legalName,
    tenderer.identifier.scheme AS tenderer_scheme,
    tenderer.identifier.uri AS tenderer_uri,
    tenderer.name AS tenderer_name,
    c.compiledRelease.tender.title AS tender_title,
    c.compiledRelease.tender.id AS tender_id,
    c.compiledRelease.buyer.name AS buyer_name,
    c.compiledRelease.ocid AS ocid,
    c.compiledRelease.date AS date
  FROM records_table c
  LATERAL VIEW explode(c.compiledRelease.tender.tenderers) exploded_tenderers AS tenderer
""")

# Create a temporary view for the extracted data
tenderers_df.createOrReplaceTempView("temp_compiledreleases")

# Perform the merge operation
spark.sql("""
    MERGE INTO TendererCompiledReleaseTable AS target
    USING temp_compiledreleases AS source
    ON target.tenderer_identifier_id = source.tenderer_identifier_id
    AND target.ocid = source.ocid
    AND target.date = source.date
    WHEN MATCHED THEN
      UPDATE SET
        target.tenderer_countryName = source.tenderer_countryName,
        target.tenderer_locality = source.tenderer_locality,
        target.tenderer_postalCode = source.tenderer_postalCode,
        target.tenderer_region = source.tenderer_region,
        target.tenderer_streetAddress = source.tenderer_streetAddress,
        target.tenderer_contact_telephone = source.tenderer_contact_telephone,
        target.tenderer_identifier_id = source.tenderer_identifier_id,
        target.tenderer_legalName = source.tenderer_legalName,
        target.tenderer_scheme = source.tenderer_scheme,
        target.tenderer_uri = source.tenderer_uri,
        target.tenderer_name = source.tenderer_name,
        target.tender_title = source.tender_title,
        target.buyer_name = source.buyer_name
    WHEN NOT MATCHED THEN
      INSERT (
        tenderer_countryName,
        tenderer_locality,
        tenderer_postalCode,
        tenderer_region,
        tenderer_streetAddress,
        tenderer_contact_telephone,
        tenderer_identifier_id,
        tenderer_legalName,
        tenderer_scheme,
        tenderer_uri,
        tenderer_name,
        tender_title,
        buyer_name
      ) VALUES (
        source.tenderer_countryName,
        source.tenderer_locality,
        source.tenderer_postalCode,
        source.tenderer_region,
        source.tenderer_streetAddress,
        source.tenderer_contact_telephone,
        source.tenderer_identifier_id,
        source.tenderer_legalName,
        source.tenderer_scheme,
        source.tenderer_uri,
        source.tenderer_name,
        source.tender_title,
        source.buyer_name
      )
""")


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
spark = SparkSession.builder \
    .appName("Extract Tenderers Fields with Tender and Buyer Name") \
    .getOrCreate()

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
        StructField("address", StructType([
            StructField("countryName", StringType(), True),
            StructField("locality", StringType(), True),
            StructField("postalCode", StringType(), True),
            StructField("region", StringType(), True),
            StructField("streetAddress", StringType(), True)
        ]), True),
        StructField("contactPoint", StructType([
            StructField("email", StringType(), True),
            StructField("faxNumber", StringType(), True),
            StructField("telephone", StringType(), True)
        ]), True),
        StructField("identifier", StructType([
            StructField("legalName", StringType(), True),
            StructField("scheme", StringType(), True),
            StructField("uri", StringType(), True)
        ]), True),
        StructField("name", StringType(), True)
    ]), True),
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
    ])), True),
    StructField("date", StringType(), True),
    StructField("id", StringType(), True),
    StructField("initiationType", StringType(), True),
    StructField("language", StringType(), True),
    StructField("ocid", StringType(), True),
    StructField("planning", StructType([
        StructField("budget", StructType([
            StructField("amount", StructType([
                StructField("amount", IntegerType(), True),
                StructField("currency", StringType(), True)
            ]), True),
            StructField("description", StringType(), True),
            StructField("id", StringType(), True),
            StructField("project", StringType(), True),
            StructField("projectID", StringType(), True)
        ]), True),
        StructField("rationale", StringType(), True)
    ]), True),
    StructField("tag", ArrayType(StringType(), True), True),
    StructField("tender", StructType([
        StructField("awardCriteria", StringType(), True),
        StructField("awardCriteriaDetails", StringType(), True),
        StructField("awardPeriod", StructType([
            StructField("endDate", StringType(), True),
            StructField("startDate", StringType(), True)
        ]), True),
        StructField("description", StringType(), True),
        StructField("documents", ArrayType(StructType([
            StructField("dateModified", StringType(), True),
            StructField("datePublished", StringType(), True),
            StructField("description", StringType(), True),
            StructField("documentType", StringType(), True),
            StructField("format", StringType(), True),
            StructField("id", StringType(), True),
            StructField("language", StringType(), True),
            StructField("title", StringType(), True),
            StructField("url", StringType(), True)
        ])), True),
        StructField("eligibilityCriteria", StringType(), True),
        StructField("enquiryPeriod", StructType([
            StructField("endDate", StringType(), True),
            StructField("startDate", StringType(), True)
        ]), True),
        StructField("hasEnquiries", BooleanType(), True),
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
        StructField("numberOfTenderers", IntegerType(), True),
        StructField("procurementMethod", StringType(), True),
        StructField("procurementMethodRationale", StringType(), True),
        StructField("procuringEntity", StructType([
            StructField("address", StructType([
                StructField("countryName", StringType(), True),
                StructField("locality", StringType(), True),
                StructField("postalCode", StringType(), True),
                StructField("region", StringType(), True),
                StructField("streetAddress", StringType(), True)
            ]), True),
            StructField("contactPoint", StructType([
                StructField("email", StringType(), True),
                StructField("faxNumber", StringType(), True),
                StructField("telephone", StringType(), True)
            ]), True),
            StructField("identifier", StructType([
                StructField("legalName", StringType(), True),
                StructField("scheme", StringType(), True),
                StructField("uri", StringType(), True)
            ]), True),
            StructField("name", StringType(), True)
        ]), True),
        StructField("status", StringType(), True),
        StructField("submissionMethod", ArrayType(StringType(), True), True),
        StructField("submissionMethodDetails", StringType(), True),
        StructField("tenderers", ArrayType(StructType([
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
        StructField("tenderPeriod", StructType([
            StructField("endDate", StringType(), True),
            StructField("startDate", StringType(), True)
        ]), True),
        StructField("title", StringType(), True),
        StructField("value", StructType([
            StructField("amount", IntegerType(), True),
            StructField("currency", StringType(), True)
        ]), True)
    ]), True)
])

# Read the table
df = spark.sql("SELECT * FROM Lh_procurement.procurement")

# Extract the compiledRelease column and create a temporary view
df.select(from_json(col("compiledRelease"), schema).alias("compiledRelease")).createOrReplaceTempView("records_table")

# Execute the SQL query to extract the desired fields from the tenderers array, along with tender name and buyer name
tenderers_df = spark.sql("""
  SELECT
    tenderer.address.countryName AS tenderer_countryName,
    tenderer.address.locality AS tenderer_locality,
    tenderer.address.postalCode AS tenderer_postalCode,
    tenderer.address.region AS tenderer_region,
    tenderer.address.streetAddress AS tenderer_streetAddress,
    tenderer.contactPoint.telephone AS tenderer_contact_telephone,
    tenderer.identifier.id AS tenderer_identifier_id,
    tenderer.identifier.legalName AS tenderer_legalName,
    tenderer.identifier.scheme AS tenderer_scheme,
    tenderer.identifier.uri AS tenderer_uri,
    tenderer.name AS tenderer_name,
    c.compiledRelease.tender.title AS tender_title,
    c.compiledRelease.tender.id AS tender_id,
    c.compiledRelease.buyer.name AS buyer_name,
    c.compiledRelease.ocid AS ocid,
    c.compiledRelease.date AS date
  FROM records_table c
  LATERAL VIEW explode(c.compiledRelease.tender.tenderers) exploded_tenderers AS tenderer
""")

#display(tenderers_df)
# Write the DataFrame to the Delta table
tenderers_df.write.format("delta").mode("overwrite").saveAsTable("TendererCompiledReleaseTablev1")


# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

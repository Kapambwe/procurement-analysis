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

from pyspark.sql.types import StructType, StructField, StringType, ArrayType
from pyspark.sql.functions import from_json, explode, col

# Define the schema for the versionedRelease structure
versionedRelease_schema = StructType([
    StructField("tender", StructType([
        StructField("title",  ArrayType(StructType([
            StructField("value", StringType(), True)
        ])), True),
        StructField("tenderers", ArrayType(StructType([
            StructField("releaseDate", StringType(), True),
            StructField("value", ArrayType(StructType([
                StructField("identifier", StructType([
                    StructField("legalName", StringType(), True),
                    StructField("scheme", StringType(), True),
                    StructField("id", StringType(), True),
                    StructField("uri", StringType(), True)
                ]), True),
                StructField("address", StructType([
                    StructField("streetAddress", StringType(), True),
                    StructField("postalCode", StringType(), True),
                    StructField("locality", StringType(), True),
                    StructField("countryName", StringType(), True),
                    StructField("region", StringType(), True)
                ]), True),
                StructField("contactPoint", StructType([
                    StructField("telephone", StringType(), True)
                ]), True),
                StructField("name", StringType(), True)
            ])), True)
        ])), True)
    ]), True)
])

# Read the table
df = spark.sql("SELECT * FROM Lh_procurement.procurement")

# Count the number of rows in the DataFrame
row_count = df.count()
print(f"The number of rows in the DataFrame is: {row_count}")

# Extract the versionedRelease column and create a temporary view
df.select(from_json(col("versionedRelease"), versionedRelease_schema).alias("versionedRelease")).createOrReplaceTempView("records_table")

# Extract the relevant fields
tenderers_df = spark.sql('''
    SELECT
        v.versionedRelease.tender.title[0].value AS tender_title,
        t.releaseDate AS tenderer_releaseDate,
        i.legalName AS tenderer_legalName,
        i.scheme AS tenderer_scheme,
        i.id AS tenderer_id,
        i.uri AS tenderer_uri,
        a.streetAddress AS tenderer_streetAddress,
        a.postalCode AS tenderer_postalCode,
        a.locality AS tenderer_locality,
        a.countryName AS tenderer_countryName,
        a.region AS tenderer_region,
        c.telephone AS tenderer_contactPoint_telephone,
        t.value.name AS tenderer_name
    FROM records_table v
    LATERAL VIEW explode(v.versionedRelease.tender.tenderers) as t
    LATERAL VIEW explode(t.value.identifier) as i
    LATERAL VIEW explode(t.value.address) as a
    LATERAL VIEW explode(t.value.contactPoint) as c
''')

# Create a temporary view for the DataFrame
tenderers_df.createOrReplaceTempView("temp_tenderers")

# Disable broadcast joins
spark.conf.set("spark.sql.autoBroadcastJoinThreshold", -1)

# Perform the merge operation
spark.sql("""
    MERGE INTO tendererversionedreleasestable AS target
    USING temp_tenderers AS source
    ON target.tenderer_id = source.tenderer_id AND target.tender_title = source.tender_title
    WHEN MATCHED THEN
      UPDATE SET
        target.tender_title = source.tender_title,
        target.tenderer_releaseDate = source.tenderer_releaseDate,
        target.tenderer_legalName = source.tenderer_legalName,
        target.tenderer_scheme = source.tenderer_scheme,
        target.tenderer_uri = source.tenderer_uri,
        target.tenderer_streetAddress = source.tenderer_streetAddress,
        target.tenderer_postalCode = source.tenderer_postalCode,
        target.tenderer_locality = source.tenderer_locality,
        target.tenderer_countryName = source.tenderer_countryName,
        target.tenderer_region = source.tenderer_region,
        target.tenderer_contactPoint_telephone = source.tenderer_contactPoint_telephone,
        target.tenderer_name = source.tenderer_name
    WHEN NOT MATCHED THEN
      INSERT (
        tender_title,
        tenderer_releaseDate,
        tenderer_legalName,
        tenderer_scheme,
        tenderer_id,
        tenderer_uri,
        tenderer_streetAddress,
        tenderer_postalCode,
        tenderer_locality,
        tenderer_countryName,
        tenderer_region,
        tenderer_contactPoint_telephone,
        tenderer_name
      )
      VALUES (
        source.tender_title,
        source.tenderer_releaseDate,
        source.tenderer_legalName,
        source.tenderer_scheme,
        source.tenderer_id,
        source.tenderer_uri,
        source.tenderer_streetAddress,
        source.tenderer_postalCode,
        source.tenderer_locality,
        source.tenderer_countryName,
        source.tenderer_region,
        source.tenderer_contactPoint_telephone,
        source.tenderer_name
      )
""")


# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

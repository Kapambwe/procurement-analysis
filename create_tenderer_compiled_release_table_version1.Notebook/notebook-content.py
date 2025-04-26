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

spark.sql("""
    CREATE TABLE TendererCompiledReleaseTablev1 (
        tenderer_countryName STRING,
        tenderer_locality STRING,
        tenderer_postalCode STRING,
        tenderer_region STRING,
        tenderer_streetAddress STRING,
        tenderer_contact_telephone STRING,
        tenderer_identifier_id STRING,
        tenderer_legalName STRING,
        tenderer_scheme STRING,
        tenderer_uri STRING,
        tenderer_name STRING,
        tender_title STRING,
        buyer_name STRING,
        date STRING,
        tender_id STRING,
        ocid STRING
    )
    USING DELTA
""")

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# Create the Delta table
spark.sql("""
    CREATE TABLE AwardCompiledReleaseTablev1 (
        date STRING,
        description STRING,
        id STRING,
        item_classification_description STRING,
        item_classification_id STRING,
        item_classification_scheme STRING,
        item_classification_uri STRING,
        item_description STRING,
        item_id STRING,
        quantity INT,
        item_unit_name STRING,
        status STRING,
        supplier_countryName STRING,
        supplier_locality STRING,
        supplier_postalCode STRING,
        supplier_region STRING,
        supplier_streetAddress STRING,
        supplier_contact_telephone STRING,
        supplier_identifier_id STRING,
        supplier_legalName STRING,
        supplier_scheme STRING,
        supplier_uri STRING,
        supplier_name STRING,
        title STRING,
        award_value_amount INT,
        award_value_currency STRING,
        tender_title STRING,
        tender_id STRING,
        buyer_name STRING,
        created_date STRING,
        ocid STRING
    )
    USING DELTA
""")

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

spark.sql("""
    CREATE TABLE ContractCompiledReleaseTable (
        awardID STRING,
        dateSigned STRING,
        description STRING,
        id STRING,
        item_classification_description STRING,
        item_classification_id STRING,
        item_classification_scheme STRING,
        item_classification_uri STRING,
        item_description STRING,
        item_id STRING,
        status STRING,
        title STRING,
        contract_value_amount INT,
        contract_value_currency STRING
    )
    USING DELTA
""")

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

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

# MAGIC %%sql
# MAGIC SELECT * FROM Lh_rocurement.procurement

# METADATA ********************

# META {
# META   "language": "sparksql",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

df = spark.sql("SELECT * FROM LH_Procurement.procurement LIMIT 1000")
display(df)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# Assuming you have already created a Spark session
df = spark.sql("SELECT * FROM Lh_procurement.procurement WHERE parentFileName = 'recordPackage_2025_1_1.json'")

# Show the top 1000 rows
df.show(1000)


# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

from pyspark.sql.functions import from_json, explode, col
from pyspark.sql.types import StructType, StructField, StringType, ArrayType, DoubleType, LongType

# Define the schema for the releases array
release_schema = ArrayType(
    StructType([
        StructField("initiationType", StringType(), True),
        StructField("tender", StructType([
            StructField("tenderPeriod", StructType([
                StructField("endDate", StringType(), True)
            ]), True),
            StructField("awardPeriod", StructType([
                StructField("startDate", StringType(), True)
            ]), True),
            StructField("eligibilityCriteria", StringType(), True),
            StructField("description", StringType(), True),
            StructField("awardCriteria", StringType(), True),
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
            StructField("procuringEntity", StructType([
                StructField("address", StructType([
                    StructField("streetAddress", StringType(), True),
                    StructField("countryName", StringType(), True),
                    StructField("postalCode", StringType(), True),
                    StructField("region", StringType(), True),
                    StructField("locality", StringType(), True)
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
            StructField("procurementMethodRationale", StringType(), True),
            StructField("submissionMethod", ArrayType(StringType()), True),
            StructField("documents", ArrayType(StructType([
                StructField("format", StringType(), True),
                StructField("url", StringType(), True),
                StructField("description", StringType(), True),
                StructField("dateModified", StringType(), True),
                StructField("id", StringType(), True),
                StructField("language", StringType(), True),
                StructField("documentType", StringType(), True),
                StructField("title", StringType(), True)
            ])), True),
            StructField("hasEnquiries", StringType(), True),
            StructField("id", StringType(), True),
            StructField("status", StringType(), True),
            StructField("submissionMethodDetails", StringType(), True),
            StructField("numberOfTenderers", LongType(), True),
            StructField("title", StringType(), True),
            StructField("enquiryPeriod", StructType([
                StructField("endDate", StringType(), True)
            ]), True),
            StructField("value", StructType([
                StructField("amount", DoubleType(), True),
                StructField("currency", StringType(), True)
            ]), True),
            StructField("awardCriteriaDetails", StringType(), True),
            StructField("procurementMethod", StringType(), True)
        ]), True),
        StructField("planning", StructType([
            StructField("budget", StructType([
                StructField("project", StringType(), True),
                StructField("description", StringType(), True),
                StructField("amount", StructType([
                    StructField("amount", DoubleType(), True),
                    StructField("currency", StringType(), True)
                ]), True),
                StructField("id", StringType(), True),
                StructField("projectID", StringType(), True)
            ]), True),
            StructField("rationale", StringType(), True)
        ]), True),
        StructField("id", StringType(), True),
        StructField("language", StringType(), True),
        StructField("buyer", StructType([
            StructField("address", StructType([
                StructField("streetAddress", StringType(), True),
                StructField("countryName", StringType(), True),
                StructField("postalCode", StringType(), True),
                StructField("region", StringType(), True),
                StructField("locality", StringType(), True)
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
        StructField("date", StringType(), True),
        StructField("ocid", StringType(), True)
    ])
)

# Read the table
df = spark.sql("SELECT * FROM Lh_procurement.procurement WHERE parentFileName = 'recordPackage_2024_9_1.json'")

# Parse the JSON string to an array
df = df.withColumn("releases_array", from_json(col("releases"), release_schema))

# Explode the array
df_exploded = df.withColumn("releases", explode(col("releases_array")))

# Select the required columns
releases_df = df_exploded.selectExpr(
    "releases.initiationType AS initiationType",
    "releases.tender.tenderPeriod.endDate AS tenderPeriod_endDate",
    "releases.tender.awardPeriod.startDate AS awardPeriod_startDate",
    "releases.tender.eligibilityCriteria AS eligibilityCriteria",
    "releases.tender.description AS tender_description",
    "releases.tender.awardCriteria AS awardCriteria",
    "releases.tender.items[0].classification.description AS item_classification_description",
    "releases.tender.items[0].classification.id AS item_classification_id",
    "releases.tender.items[0].classification.scheme AS item_classification_scheme",
    "releases.tender.items[0].classification.uri AS item_classification_uri",
    "releases.tender.items[0].description AS item_description",
    "releases.tender.items[0].id AS item_id",
    "releases.tender.procuringEntity.address.streetAddress AS procuringEntity_streetAddress",
    "releases.tender.procuringEntity.address.countryName AS procuringEntity_countryName",
    "releases.tender.procuringEntity.address.postalCode AS procuringEntity_postalCode",
    "releases.tender.procuringEntity.address.region AS procuringEntity_region",
    "releases.tender.procuringEntity.address.locality AS procuringEntity_locality",
    "releases.tender.procuringEntity.contactPoint.email AS procuringEntity_contactPoint_email",
    "releases.tender.procuringEntity.contactPoint.faxNumber AS procuringEntity_contactPoint_faxNumber",
    "releases.tender.procuringEntity.contactPoint.telephone AS procuringEntity_contactPoint_telephone",
    "releases.tender.procuringEntity.identifier.legalName AS procuringEntity_identifier_legalName",
    "releases.tender.procuringEntity.identifier.scheme AS procuringEntity_identifier_scheme",
    "releases.tender.procuringEntity.identifier.uri AS procuringEntity_identifier_uri",
    "releases.tender.procuringEntity.name AS procuringEntity_name",
    "releases.tender.procurementMethodRationale AS procurementMethodRationale",
    "releases.tender.submissionMethod[0] AS submissionMethod",
    "releases.tender.documents[0].format AS document_format",
    "releases.tender.documents[0].url AS document_url",
    "releases.tender.documents[0].description AS document_description",
    "releases.tender.documents[0].dateModified AS document_dateModified",
    "releases.tender.documents[0].id AS document_id",
    "releases.tender.documents[0].language AS document_language",
    "releases.tender.documents[0].documentType AS document_type",
    "releases.tender.documents[0].title AS document_title",
    "releases.tender.hasEnquiries AS hasEnquiries",
    "releases.tender.id AS tender_id",
    "releases.tender.status AS tender_status",
    "releases.tender.submissionMethodDetails AS submissionMethodDetails",
    "releases.tender.numberOfTenderers AS numberOfTenderers",
    "releases.tender.title AS tender_title",
    "releases.tender.enquiryPeriod.endDate AS enquiryPeriod_endDate",
    "releases.tender.value.amount AS tender_value_amount",
    "releases.tender.value.currency AS tender_value_currency",
    "releases.tender.awardCriteriaDetails AS awardCriteriaDetails",
    "releases.tender.procurementMethod AS procurementMethod",
    "releases.planning.budget.project AS planning_budget_project",
    "releases.planning.budget.description AS planning_budget_description",
    "releases.planning.budget.amount.amount AS planning_budget_amount",
    "releases.planning.budget.amount.currency AS planning_budget_currency",
    "releases.planning.budget.id AS planning_budget_id",
    "releases.planning.budget.projectID AS planning_budget_projectID",
    "releases.planning.rationale AS planning_rationale",
    "releases.id AS release_id",
    "releases.language AS language",
    "releases.buyer.address.streetAddress AS buyer_streetAddress",
    "releases.buyer.address.countryName AS buyer_countryName",
    "releases.buyer.address.postalCode AS buyer_postalCode",
    "releases.buyer.address.region AS buyer_region",
    "releases.buyer.address.locality AS buyer_locality",
    "releases.buyer.contactPoint.email AS buyer_contactPoint_email",
    "releases.buyer.contactPoint.faxNumber AS buyer_contactPoint_faxNumber",
    "releases.buyer.contactPoint.telephone AS buyer_contactPoint_telephone",
    "releases.buyer.identifier.legalName AS buyer_identifier_legalName",
    "releases.buyer.identifier.scheme AS buyer_identifier_scheme",
    "releases.buyer.identifier.uri AS buyer_identifier_uri",
    "releases.buyer.name AS buyer_name",
    "releases.date AS release_date",
    "releases.ocid AS release_ocid"
)

# Display the result
display(releases_df)

releases_df.createOrReplaceTempView("temp_release")

spark.sql("""
        INSERT INTO ReleaseTable
        SELECT * FROM temp_release
    """)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

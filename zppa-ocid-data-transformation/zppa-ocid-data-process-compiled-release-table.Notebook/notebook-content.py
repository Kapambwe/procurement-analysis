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

from pyspark.sql import SparkSession
from pyspark.sql.functions import from_json, col
from pyspark.sql.types import *


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
df = spark.sql("SELECT * FROM Lh_procurement.procurement WHERE parentFileName = 'recordPackage_2025_2_1.json'")

# Count the number of rows in the DataFrame
row_count = df.count()
print(f"The number of rows in the DataFrame is: {row_count}")

# Extract the compiledRelease column and create a temporary view
df.select(from_json(col("compiledRelease"), schema).alias("compiledRelease")).createOrReplaceTempView("records_table")


# Extract the relevant fields
compiledRelease_df = spark.sql('''
  SELECT
    c.compiledRelease.initiationType,
    c.compiledRelease.tender.tenderPeriod.endDate AS tender_endDate,
    c.compiledRelease.tender.tenderPeriod.startDate AS tender_startDate,
    c.compiledRelease.tender.awardPeriod.startDate AS award_startDate,
    c.compiledRelease.tender.awardPeriod.endDate AS award_endDate,
    c.compiledRelease.tender.eligibilityCriteria,
    c.compiledRelease.tender.description AS tender_description,
    c.compiledRelease.tender.awardCriteria,
    c.compiledRelease.tender.items[0].quantity AS item_quantity,
    c.compiledRelease.tender.items[0].description AS item_description,
    c.compiledRelease.tender.items[0].id AS item_id,
    c.compiledRelease.tender.items[0].classification.description AS item_classification_description,
    c.compiledRelease.tender.items[0].classification.id AS item_classification_id,
    c.compiledRelease.tender.items[0].classification.scheme AS item_classification_scheme,
    c.compiledRelease.tender.items[0].classification.uri AS item_classification_uri,
    c.compiledRelease.tender.items[0].unit.name AS item_unit_name,
    c.compiledRelease.tender.procuringEntity.address.streetAddress AS procuringEntity_streetAddress,
    c.compiledRelease.tender.procuringEntity.address.countryName AS procuringEntity_countryName,
    c.compiledRelease.tender.procuringEntity.address.postalCode AS procuringEntity_postalCode,
    c.compiledRelease.tender.procuringEntity.address.region AS procuringEntity_region,
    c.compiledRelease.tender.procuringEntity.address.locality AS procuringEntity_locality,
    c.compiledRelease.tender.procuringEntity.contactPoint.email AS procuringEntity_contact_email,
    c.compiledRelease.tender.procuringEntity.contactPoint.faxNumber AS procuringEntity_contact_fax,
    c.compiledRelease.tender.procuringEntity.contactPoint.telephone AS procuringEntity_contact_telephone,
    c.compiledRelease.tender.procuringEntity.identifier.legalName AS procuringEntity_legalName,
    c.compiledRelease.tender.procuringEntity.identifier.scheme AS procuringEntity_scheme,
    c.compiledRelease.tender.procuringEntity.identifier.uri AS procuringEntity_uri,
    c.compiledRelease.tender.procuringEntity.name AS procuringEntity_name,
    c.compiledRelease.tender.procurementMethodRationale,
    c.compiledRelease.tender.submissionMethod[0] AS submissionMethod,
    c.compiledRelease.tender.hasEnquiries,
    c.compiledRelease.tender.id AS tender_id,
    c.compiledRelease.tender.status AS tender_status,
    c.compiledRelease.tender.submissionMethodDetails,
    c.compiledRelease.tender.numberOfTenderers,
    c.compiledRelease.tender.title AS tender_title,
    c.compiledRelease.tender.enquiryPeriod.endDate AS enquiry_endDate,
    c.compiledRelease.tender.enquiryPeriod.startDate AS enquiry_startDate,
    c.compiledRelease.tender.value.amount AS tender_value_amount,
    c.compiledRelease.tender.value.currency AS tender_value_currency,
    c.compiledRelease.tender.awardCriteriaDetails,
    c.compiledRelease.tender.procurementMethod,
    c.compiledRelease.tag[0] AS tag,
    c.compiledRelease.planning.budget.project AS budget_project,
    c.compiledRelease.planning.budget.description AS budget_description,
    c.compiledRelease.planning.budget.amount.amount AS budget_amount,
    c.compiledRelease.planning.budget.amount.currency AS budget_currency,
    c.compiledRelease.planning.budget.id AS budget_id,
    c.compiledRelease.planning.budget.projectID AS budget_projectID,
    c.compiledRelease.planning.rationale AS planning_rationale,
    c.compiledRelease.id AS compiled_id,
    c.compiledRelease.language,
    c.compiledRelease.buyer.address.streetAddress AS buyer_streetAddress,
    c.compiledRelease.buyer.address.countryName AS buyer_countryName,
    c.compiledRelease.buyer.address.postalCode AS buyer_postalCode,
    c.compiledRelease.buyer.address.region AS buyer_region,
    c.compiledRelease.buyer.address.locality AS buyer_locality,
    c.compiledRelease.buyer.contactPoint.email AS buyer_contact_email,
    c.compiledRelease.buyer.contactPoint.faxNumber AS buyer_contact_fax,
    c.compiledRelease.buyer.contactPoint.telephone AS buyer_contact_telephone,
    c.compiledRelease.buyer.identifier.legalName AS buyer_legalName,
    c.compiledRelease.buyer.identifier.scheme AS buyer_scheme,
    c.compiledRelease.buyer.identifier.uri AS buyer_uri,
    c.compiledRelease.buyer.name AS buyer_name,
    c.compiledRelease.date,
    c.compiledRelease.ocid
  FROM records_table c
''')

# Create a temporary view for the DataFrame
compiledRelease_df.createOrReplaceTempView("temp_compiledreleases")

# Perform the merge operation
spark.sql("""
    MERGE INTO compiledreleasetable AS target
    USING temp_compiledreleases AS source
    ON target.ocid = source.ocid AND target.tender_id = source.tender_id
    AND target.date = source.date
    WHEN MATCHED THEN
      UPDATE SET
        target.initiationType = source.initiationType,
        target.tender_endDate = source.tender_endDate,
        target.tender_startDate = source.tender_startDate,
        target.award_startDate = source.award_startDate,
        target.award_endDate = source.award_endDate,
        target.eligibilityCriteria = source.eligibilityCriteria,
        target.tender_description = source.tender_description,
        target.awardCriteria = source.awardCriteria,
        target.item_quantity = source.item_quantity,
        target.item_description = source.item_description,
        target.item_id = source.item_id,
        target.item_classification_description = source.item_classification_description,
        target.item_classification_id = source.item_classification_id,
        target.item_classification_scheme = source.item_classification_scheme,
        target.item_classification_uri = source.item_classification_uri,
        target.item_unit_name = source.item_unit_name,
        target.procuringEntity_streetAddress = source.procuringEntity_streetAddress,
        target.procuringEntity_countryName = source.procuringEntity_countryName,
        target.procuringEntity_postalCode = source.procuringEntity_postalCode,
        target.procuringEntity_region = source.procuringEntity_region,
        target.procuringEntity_locality = source.procuringEntity_locality,
        target.procuringEntity_contact_email = source.procuringEntity_contact_email,
        target.procuringEntity_contact_fax = source.procuringEntity_contact_fax,
        target.procuringEntity_contact_telephone = source.procuringEntity_contact_telephone,
        target.procuringEntity_legalName = source.procuringEntity_legalName,
        target.procuringEntity_scheme = source.procuringEntity_scheme,
        target.procuringEntity_uri = source.procuringEntity_uri,
        target.procuringEntity_name = source.procuringEntity_name,
        target.procurementMethodRationale = source.procurementMethodRationale,
        target.submissionMethod = source.submissionMethod,
        target.hasEnquiries = source.hasEnquiries,
        target.tender_status = source.tender_status,
        target.submissionMethodDetails = source.submissionMethodDetails,
        target.numberOfTenderers = source.numberOfTenderers,
        target.tender_title = source.tender_title,
        target.enquiry_endDate = source.enquiry_endDate,
        target.enquiry_startDate = source.enquiry_startDate,
        target.tender_value_amount = source.tender_value_amount,
        target.tender_value_currency = source.tender_value_currency,
        target.awardCriteriaDetails = source.awardCriteriaDetails,
        target.procurementMethod = source.procurementMethod,
        target.tag = source.tag,
        target.budget_project = source.budget_project,
        target.budget_description = source.budget_description,
        target.budget_amount = source.budget_amount,
        target.budget_currency = source.budget_currency,
        target.budget_id = source.budget_id,
        target.budget_projectID = source.budget_projectID,
        target.planning_rationale = source.planning_rationale,
        target.language = source.language,
        target.buyer_streetAddress = source.buyer_streetAddress,
        target.buyer_countryName = source.buyer_countryName,
        target.buyer_postalCode = source.buyer_postalCode,
        target.buyer_region = source.buyer_region,
        target.buyer_locality = source.buyer_locality,
        target.buyer_contact_email = source.buyer_contact_email,
        target.buyer_contact_fax = source.buyer_contact_fax,
        target.buyer_contact_telephone = source.buyer_contact_telephone,
        target.buyer_legalName = source.buyer_legalName,
        target.buyer_scheme = source.buyer_scheme,
        target.buyer_uri = source.buyer_uri,
        target.buyer_name = source.buyer_name,
        target.date = source.date,
        target.ocid = source.ocid
    WHEN NOT MATCHED THEN
      INSERT (
        initiationType,
        tender_endDate,
        tender_startDate,
        award_startDate,
        award_endDate,
        eligibilityCriteria,
        tender_description,
        awardCriteria,
        item_quantity,
        item_description,
        item_id,
        item_classification_description,
        item_classification_id,
        item_classification_scheme,
        item_classification_uri,
        item_unit_name,
        procuringEntity_streetAddress,
        procuringEntity_countryName,
        procuringEntity_postalCode,
        procuringEntity_region,
        procuringEntity_locality,
        procuringEntity_contact_email,
        procuringEntity_contact_fax,
        procuringEntity_contact_telephone,
        procuringEntity_legalName,
        procuringEntity_scheme,
        procuringEntity_uri,
        procuringEntity_name,
        procurementMethodRationale,
        submissionMethod,
        hasEnquiries,
        tender_id,
        tender_status,
        submissionMethodDetails,
        numberOfTenderers,
        tender_title,
        enquiry_endDate,
        enquiry_startDate,
        tender_value_amount,
        tender_value_currency,
        awardCriteriaDetails,
        procurementMethod,
        tag,
        budget_project,
        budget_description,
        budget_amount,
        budget_currency,
        budget_id,
        budget_projectID,
        planning_rationale,
        compiled_id,
        language,
        buyer_streetAddress,
        buyer_countryName,
        buyer_postalCode,
        buyer_region,
        buyer_locality,
        buyer_contact_email,
        buyer_contact_fax,
        buyer_contact_telephone,
        buyer_legalName,
        buyer_scheme,
        buyer_uri,
        buyer_name,
        date,
        ocid
      )
      VALUES (
        source.initiationType,
        source.tender_endDate,
        source.tender_startDate,
        source.award_startDate,
        source.award_endDate,
        source.eligibilityCriteria,
        source.tender_description,
        source.awardCriteria,
        source.item_quantity,
        source.item_description,
        source.item_id,
        source.item_classification_description,
        source.item_classification_id,
        source.item_classification_scheme,
        source.item_classification_uri,
        source.item_unit_name,
        source.procuringEntity_streetAddress,
        source.procuringEntity_countryName,
        source.procuringEntity_postalCode,
        source.procuringEntity_region,
        source.procuringEntity_locality,
        source.procuringEntity_contact_email,
        source.procuringEntity_contact_fax,
        source.procuringEntity_contact_telephone,
        source.procuringEntity_legalName,
        source.procuringEntity_scheme,
        source.procuringEntity_uri,
        source.procuringEntity_name,
        source.procurementMethodRationale,
        source.submissionMethod,
        source.hasEnquiries,
        source.tender_id,
        source.tender_status,
        source.submissionMethodDetails,
        source.numberOfTenderers,
        source.tender_title,
        source.enquiry_endDate,
        source.enquiry_startDate,
        source.tender_value_amount,
        source.tender_value_currency,
        source.awardCriteriaDetails,
        source.procurementMethod,
        source.tag,
        source.budget_project,
        source.budget_description,
        source.budget_amount,
        source.budget_currency,
        source.budget_id,
        source.budget_projectID,
        source.planning_rationale,
        source.compiled_id,
        source.language,
        source.buyer_streetAddress,
        source.buyer_countryName,
        source.buyer_postalCode,
        source.buyer_region,
        source.buyer_locality,
        source.buyer_contact_email,
        source.buyer_contact_fax,
        source.buyer_contact_telephone,
        source.buyer_legalName,
        source.buyer_scheme,
        source.buyer_uri,
        source.buyer_name,
        source.date,
        source.ocid
      )
""")


# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

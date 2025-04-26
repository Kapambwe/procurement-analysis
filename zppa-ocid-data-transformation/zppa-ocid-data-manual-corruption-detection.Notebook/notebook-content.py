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
# MAGIC SELECT   
# MAGIC     tcr.[tenderer_name],
# MAGIC     tcr.[tender_title],
# MAGIC     tcr.[buyer_name],
# MAGIC     crt.[tender_endDate],
# MAGIC     crt.[tender_status],
# MAGIC     crt.[tender_value_amount],
# MAGIC     crt.[tender_value_currency],
# MAGIC     crt.[procurementMethod],
# MAGIC     crt.[numberOfTenderers]
# MAGIC FROM 
# MAGIC     [dbo].[tenderercompiledreleasetable] tcr
# MAGIC INNER JOIN 
# MAGIC     [dbo].[compiledreleasetable] crt
# MAGIC ON 
# MAGIC     tcr.[tender_title] = crt.[tender_title]


# METADATA ********************

# META {
# META   "language": "sparksql",
# META   "language_group": "synapse_pyspark"
# META }

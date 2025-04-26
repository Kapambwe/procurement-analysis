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

# MAGIC %%sql
# MAGIC DECLARE @NextTenderCompanyId INT;
# MAGIC 
# MAGIC -- Get the maximum TenderCompanyId from the table
# MAGIC SELECT @NextTenderCompanyId = ISNULL(MAX([TenderCompanyId]), 0) + 1
# MAGIC FROM [Wh_Procurement].[tender].[TenderCompany];
# MAGIC 
# MAGIC -- Insert unique rows into the TenderCompany table
# MAGIC INSERT INTO [Wh_Procurement].[tender].[TenderCompany] (
# MAGIC     [TenderCompanyId],
# MAGIC     [CompanyRoleId],
# MAGIC     [ClosingDate],
# MAGIC     [TenderId],
# MAGIC     [CompanyId]
# MAGIC )
# MAGIC SELECT 
# MAGIC     ROW_NUMBER() OVER (ORDER BY (SELECT NULL)) + @NextTenderCompanyId - 1 AS [TenderCompanyId],
# MAGIC     cr.[CompanyRoleId],
# MAGIC     ISNULL(acrt.[date], GETDATE()) AS [ClosingDate], -- Use current date if ClosingDate is NULL
# MAGIC     t.[TenderId],
# MAGIC     c.[CompanyId]
# MAGIC FROM 
# MAGIC     [dbo].[awardcompiledreleasetablev1] acrt
# MAGIC INNER JOIN 
# MAGIC     [dbo].[compiledreleasetable] crt ON acrt.[tender_title] = crt.[tender_title] AND acrt.[tender_id] = crt.[tender_id]
# MAGIC INNER JOIN 
# MAGIC     [Wh_Procurement].[tender].[Tender] t ON crt.[tender_title] = t.[Name] AND crt.[tender_id] =t.[ExternalId]
# MAGIC INNER JOIN 
# MAGIC     [Wh_Procurement].[company].[Company] c ON LOWER(acrt.[supplier_name]) = LOWER(c.[Name]) 
# MAGIC INNER JOIN 
# MAGIC     [Wh_Procurement].[tender].[CompanyRole] cr ON cr.[Name] = 'AwardedCompany'
# MAGIC WHERE 
# MAGIC     NOT EXISTS (
# MAGIC         SELECT 1
# MAGIC         FROM [Wh_Procurement].[tender].[TenderCompany] tc
# MAGIC         WHERE tc.[TenderId] = t.[TenderId]
# MAGIC           AND tc.[CompanyId] = c.[CompanyId]
# MAGIC           AND tc.[CompanyRoleId]=13
# MAGIC     );

# METADATA ********************

# META {
# META   "language": "sparksql",
# META   "language_group": "synapse_pyspark"
# META }

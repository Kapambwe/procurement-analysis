CREATE TABLE [tender].[ProcurementMethodRationale] (

	[ProcurementMethodRationaleId] int NOT NULL, 
	[Name] varchar(8000) NULL, 
	[Description] varchar(8000) NULL
);


GO
ALTER TABLE [tender].[ProcurementMethodRationale] ADD CONSTRAINT PK_ProcurementMethodRationale primary key NONCLUSTERED ([ProcurementMethodRationaleId]);
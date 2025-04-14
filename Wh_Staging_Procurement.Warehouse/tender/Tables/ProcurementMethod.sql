CREATE TABLE [tender].[ProcurementMethod] (

	[ProcurementMethodId] int NOT NULL, 
	[Name] varchar(200) NOT NULL, 
	[Description] varchar(100) NULL
);


GO
ALTER TABLE [tender].[ProcurementMethod] ADD CONSTRAINT PK_ProcurementMethod primary key NONCLUSTERED ([ProcurementMethodId]);
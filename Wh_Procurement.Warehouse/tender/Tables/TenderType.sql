CREATE TABLE [tender].[TenderType] (

	[TenderTypeId] int NOT NULL, 
	[Name] varchar(200) NOT NULL
);


GO
ALTER TABLE [tender].[TenderType] ADD CONSTRAINT PK_TenderType primary key NONCLUSTERED ([TenderTypeId]);
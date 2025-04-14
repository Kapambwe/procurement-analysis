CREATE TABLE [tender].[DocumentType] (

	[DocumentTypeId] int NOT NULL, 
	[Name] varchar(100) NOT NULL, 
	[Code] varchar(100) NOT NULL, 
	[Description] varchar(8000) NOT NULL
);


GO
ALTER TABLE [tender].[DocumentType] ADD CONSTRAINT PK_DocumentType primary key NONCLUSTERED ([DocumentTypeId]);
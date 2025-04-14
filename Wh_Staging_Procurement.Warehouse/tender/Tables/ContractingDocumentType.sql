CREATE TABLE [tender].[ContractingDocumentType] (

	[ContractingDocumentTypeId] int NOT NULL, 
	[Section] varchar(100) NOT NULL, 
	[Category] varchar(100) NOT NULL, 
	[DocumentTypeId] int NOT NULL
);


GO
ALTER TABLE [tender].[ContractingDocumentType] ADD CONSTRAINT PK_ContractingDocumentType primary key NONCLUSTERED ([ContractingDocumentTypeId]);
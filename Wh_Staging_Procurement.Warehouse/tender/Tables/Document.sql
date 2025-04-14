CREATE TABLE [tender].[Document] (

	[DocumentId] int NOT NULL, 
	[Title] varchar(4000) NULL, 
	[Description] varchar(4000) NULL, 
	[Url] varchar(250) NULL, 
	[DocumentType] varchar(100) NULL, 
	[DatePublished] datetime2(6) NULL, 
	[DateModified] datetime2(6) NULL, 
	[Format] varchar(50) NULL, 
	[Language] varchar(20) NULL, 
	[ExternalId] varchar(100) NULL, 
	[KnowledgeSourceDetailId] int NULL, 
	[IsActive] bit NULL, 
	[DocumentTypeId] int NULL, 
	[IsFormated] bit NULL
);


GO
ALTER TABLE [tender].[Document] ADD CONSTRAINT PK_Document primary key NONCLUSTERED ([DocumentId]);
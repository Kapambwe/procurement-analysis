CREATE TABLE [tender].[Document] (

	[DocumentId] int NOT NULL, 
	[DateModified] datetime2(6) NULL, 
	[DatePublished] datetime2(6) NULL, 
	[Description] varchar(8000) NULL, 
	[Type] varchar(50) NULL, 
	[ExternalId] varchar(50) NOT NULL, 
	[Name] varchar(8000) NULL, 
	[Language] varchar(50) NULL, 
	[Url] varchar(255) NULL, 
	[TenderId] int NULL, 
	[ExternalTenderId] int NULL
);


GO
ALTER TABLE [tender].[Document] ADD CONSTRAINT PK_Document primary key NONCLUSTERED ([DocumentId]);
GO
ALTER TABLE [tender].[Document] ADD CONSTRAINT FK_Document_TenderId FOREIGN KEY ([TenderId]) REFERENCES [tender].[Tenders]([TenderId]);
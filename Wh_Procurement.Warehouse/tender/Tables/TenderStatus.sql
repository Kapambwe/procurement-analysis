CREATE TABLE [tender].[TenderStatus] (

	[TenderStatusId] int NOT NULL, 
	[Name] varchar(200) NOT NULL, 
	[Description] varchar(1000) NULL
);


GO
ALTER TABLE [tender].[TenderStatus] ADD CONSTRAINT PK_TenderStatus primary key NONCLUSTERED ([TenderStatusId]);
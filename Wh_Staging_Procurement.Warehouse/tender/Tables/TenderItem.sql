CREATE TABLE [tender].[TenderItem] (

	[TenderItemId] int NOT NULL, 
	[ContractingProcessId] int NULL, 
	[TenderId] int NULL, 
	[ContractTenderId] int NULL, 
	[AwardTenderId] int NULL, 
	[ProductId] int NULL, 
	[Description] varchar(4000) NULL, 
	[Classification] varchar(4000) NULL, 
	[Scheme] varchar(4000) NULL, 
	[Unit] varchar(50) NULL, 
	[ExternalId] varchar(100) NULL, 
	[Quantity] int NOT NULL
);


GO
ALTER TABLE [tender].[TenderItem] ADD CONSTRAINT PK_TenderItem primary key NONCLUSTERED ([TenderItemId]);
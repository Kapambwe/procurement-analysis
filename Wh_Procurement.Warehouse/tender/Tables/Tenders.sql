CREATE TABLE [tender].[Tenders] (

	[TenderId] int NOT NULL, 
	[Name] varchar(8000) NOT NULL, 
	[Amount] decimal(18,0) NULL, 
	[BudgetAmount] decimal(18,0) NULL, 
	[Description] varchar(8000) NULL, 
	[ExternalId] varchar(8000) NULL, 
	[ReleaseData] varchar(8000) NULL, 
	[ReleaseOcid] varchar(8000) NULL, 
	[InitiationType] varchar(8000) NULL, 
	[BudgetCurrencyId] int NULL, 
	[TenderCurrencyId] int NULL, 
	[BudgetDescription] varchar(8000) NULL
);


GO
ALTER TABLE [tender].[Tenders] ADD CONSTRAINT PK_TenderId primary key NONCLUSTERED ([TenderId]);
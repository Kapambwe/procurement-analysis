CREATE TABLE [tender].[ContractTender] (

	[ContractTenderId] int NOT NULL, 
	[AwardTenderId] int NULL, 
	[Title] varchar(4000) NULL, 
	[Description] varchar(8000) NULL, 
	[ContractStatus] varchar(100) NULL, 
	[ContractSignedDate] datetime2(6) NULL, 
	[ContractAmount] decimal(20,4) NULL, 
	[TenderPeriodId] int NULL, 
	[ExternalId] varchar(100) NULL, 
	[CurrencyId] int NULL
);


GO
ALTER TABLE [tender].[ContractTender] ADD CONSTRAINT PK_ContractTender primary key NONCLUSTERED ([ContractTenderId]);
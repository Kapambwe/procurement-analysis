CREATE TABLE [tender].[AwardTender] (

	[AwardTenderId] int NOT NULL, 
	[Title] varchar(8000) NULL, 
	[Description] varchar(8000) NULL, 
	[AwardStatus] varchar(100) NULL, 
	[AwardDate] datetime2(6) NULL, 
	[AwardAmount] decimal(20,4) NULL, 
	[TenderPeriodId] int NULL, 
	[ExternalId] varchar(100) NULL, 
	[CurrencyId] int NOT NULL
);


GO
ALTER TABLE [tender].[AwardTender] ADD CONSTRAINT PK_AwardTender primary key NONCLUSTERED ([AwardTenderId]);
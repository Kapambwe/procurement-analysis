CREATE TABLE [tender].[TenderPeriod] (

	[TenderPeriodId] int NOT NULL, 
	[StartDate] datetime2(6) NULL, 
	[EndDate] datetime2(6) NULL, 
	[TenderYear] int NULL
);


GO
ALTER TABLE [tender].[TenderPeriod] ADD CONSTRAINT PK_TenderPeriod primary key NONCLUSTERED ([TenderPeriodId]);
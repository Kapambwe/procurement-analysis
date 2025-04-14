CREATE TABLE [tender].[Planning] (

	[PlanningId] int NOT NULL, 
	[Amount] decimal(20,4) NULL, 
	[Description] varchar(8000) NULL, 
	[ReleaseId] varchar(4000) NULL, 
	[ReleaseDate] datetime2(6) NULL, 
	[ReleaseTag] varchar(4000) NULL, 
	[CurrencyId] int NULL, 
	[ExternalId] varchar(4000) NULL
);


GO
ALTER TABLE [tender].[Planning] ADD CONSTRAINT PK_Planning primary key NONCLUSTERED ([PlanningId]);
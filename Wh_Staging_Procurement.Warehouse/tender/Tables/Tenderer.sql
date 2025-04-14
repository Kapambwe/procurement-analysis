CREATE TABLE [tender].[Tenderer] (

	[TendererId] int NOT NULL, 
	[OrganizationId] int NULL, 
	[CompanyId] int NULL, 
	[TenderId] int NULL, 
	[AwardTenderId] int NULL, 
	[ContractTenderId] int NULL, 
	[ProjectId] int NULL, 
	[ContractingProcessId] int NULL
);


GO
ALTER TABLE [tender].[Tenderer] ADD CONSTRAINT PK_Tenderer primary key NONCLUSTERED ([TendererId]);
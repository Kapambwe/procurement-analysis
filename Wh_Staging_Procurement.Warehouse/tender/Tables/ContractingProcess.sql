CREATE TABLE [tender].[ContractingProcess] (

	[ContractingProcessId] int NOT NULL, 
	[InitiationType] varchar(4000) NOT NULL, 
	[TenderId] int NULL, 
	[PlanningId] int NULL, 
	[DateTime] datetime2(6) NULL, 
	[OcId] varchar(4000) NULL, 
	[Id] varchar(4000) NULL, 
	[Langauge] varchar(100) NULL, 
	[BuyerId] int NULL, 
	[CompanyId] int NULL, 
	[ContractTenderId] int NULL, 
	[AwardTenderId] int NULL
);


GO
ALTER TABLE [tender].[ContractingProcess] ADD CONSTRAINT PK_ContractingProcess primary key NONCLUSTERED ([ContractingProcessId]);
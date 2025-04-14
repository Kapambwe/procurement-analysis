CREATE TABLE [tender].[TenderCompany] (

	[TenderCompanyId] int NOT NULL, 
	[CompanyId] int NOT NULL, 
	[TenderId] int NOT NULL, 
	[CompanyRoleId] int NOT NULL, 
	[ContractingStageId] int NOT NULL, 
	[Amount] decimal(18,3) NOT NULL, 
	[DateSigned] datetime2(6) NOT NULL
);


GO
ALTER TABLE [tender].[TenderCompany] ADD CONSTRAINT PK_TenderCompany primary key NONCLUSTERED ([TenderCompanyId]);
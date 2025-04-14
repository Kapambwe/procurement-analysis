CREATE TABLE [person].[PersonCompany] (

	[PersonCompanyId] int NOT NULL, 
	[CompanyId] int NOT NULL, 
	[PersonRoleId] int NOT NULL, 
	[PersonId] int NOT NULL
);


GO
ALTER TABLE [person].[PersonCompany] ADD CONSTRAINT PK_PersonCompany primary key NONCLUSTERED ([PersonCompanyId]);
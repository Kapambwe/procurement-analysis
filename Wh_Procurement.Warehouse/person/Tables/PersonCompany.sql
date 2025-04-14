CREATE TABLE [person].[PersonCompany] (

	[PersonCompanyId] int NOT NULL, 
	[CompanyId] int NOT NULL, 
	[PersonRoleId] int NOT NULL, 
	[PersonId] int NOT NULL
);


GO
ALTER TABLE [person].[PersonCompany] ADD CONSTRAINT PK_PersonCompany primary key NONCLUSTERED ([PersonCompanyId]);
GO
ALTER TABLE [person].[PersonCompany] ADD CONSTRAINT FK_PersonCompany_Company FOREIGN KEY ([CompanyId]) REFERENCES [company].[Company]([CompanyId]);
GO
ALTER TABLE [person].[PersonCompany] ADD CONSTRAINT FK_PersonCompany_PersonId FOREIGN KEY ([PersonId]) REFERENCES [person].[Person]([PersonId]);
GO
ALTER TABLE [person].[PersonCompany] ADD CONSTRAINT FK_PersonCompany_PersonRole FOREIGN KEY ([PersonRoleId]) REFERENCES [tender].[PersonRole]([PersonRoleId]);
CREATE TABLE [tender].[CompanyRole] (

	[CompanyRoleId] int NOT NULL, 
	[Name] varchar(100) NULL, 
	[Description] varchar(100) NULL, 
	[Code] varchar(100) NULL, 
	[RelationShipName] varchar(100) NULL
);


GO
ALTER TABLE [tender].[CompanyRole] ADD CONSTRAINT PK_CompanyRole primary key NONCLUSTERED ([CompanyRoleId]);
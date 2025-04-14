CREATE TABLE [company].[Company] (

	[CompanyId] int NOT NULL, 
	[Name] varchar(1000) NOT NULL, 
	[CountryId] int NOT NULL, 
	[BusinessTypeId] int NULL, 
	[CompanyTypeId] int NULL, 
	[Address] varchar(100) NULL, 
	[Active] bit NULL, 
	[PhoneNumber] varchar(50) NULL, 
	[EmailAddress] varchar(500) NULL, 
	[City] varchar(500) NULL, 
	[LegalName] varchar(500) NULL, 
	[PostalCode] varchar(100) NULL, 
	[ParentCompanyId] int NULL, 
	[Locality] varchar(500) NULL, 
	[Region] varchar(500) NULL
);


GO
ALTER TABLE [company].[Company] ADD CONSTRAINT PK_Company primary key NONCLUSTERED ([CompanyId]);
GO
ALTER TABLE [company].[Company] ADD CONSTRAINT FK_Company_BusinessType FOREIGN KEY ([BusinessTypeId]) REFERENCES [list].[BusinessType]([BusinessTypeId]);
GO
ALTER TABLE [company].[Company] ADD CONSTRAINT FK_Company_CompanyType FOREIGN KEY ([CompanyTypeId]) REFERENCES [list].[CompanyType]([CompanyTypeId]);
GO
ALTER TABLE [company].[Company] ADD CONSTRAINT FK_Company_Country FOREIGN KEY ([CountryId]) REFERENCES [list].[Country]([CountryId]);
GO
ALTER TABLE [company].[Company] ADD CONSTRAINT FK_Company_ParentCompany FOREIGN KEY ([ParentCompanyId]) REFERENCES [company].[Company]([CompanyId]);
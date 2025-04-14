CREATE TABLE [tender].[TenderCompany] (

	[TenderCompanyId] int NOT NULL, 
	[CompanyRoleId] int NOT NULL, 
	[ClosingDate] date NOT NULL, 
	[TenderId] int NOT NULL, 
	[CompanyId] int NOT NULL
);


GO
ALTER TABLE [tender].[TenderCompany] ADD CONSTRAINT FK_TenderCompany_Company FOREIGN KEY ([CompanyId]) REFERENCES [company].[Company]([CompanyId]);
GO
ALTER TABLE [tender].[TenderCompany] ADD CONSTRAINT FK_TenderCompany_CompanyRole FOREIGN KEY ([CompanyRoleId]) REFERENCES [tender].[CompanyRole]([CompanyRoleId]);
GO
ALTER TABLE [tender].[TenderCompany] ADD CONSTRAINT FK_TenderCompany_Tender FOREIGN KEY ([TenderId]) REFERENCES [tender].[Tender]([TenderId]);
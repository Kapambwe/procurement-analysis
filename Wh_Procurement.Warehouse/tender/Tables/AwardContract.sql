CREATE TABLE [tender].[AwardContract] (

	[AwardContractId] int NOT NULL, 
	[Name] varchar(255) NOT NULL, 
	[Description] varchar(8000) NULL, 
	[ExternalAwardId] int NULL, 
	[TenderStatusId] int NULL, 
	[TenderId] int NULL, 
	[AwardAmount] decimal(18,2) NULL, 
	[CurrencyId] int NULL, 
	[BuyerId] int NULL, 
	[AwardedId] int NULL, 
	[Quantity] int NULL, 
	[ProductId] int NULL, 
	[AwardDate] datetime2(6) NULL, 
	[ContractDateSigned] datetime2(6) NULL, 
	[ContractName] varchar(255) NULL, 
	[ContractDescription] varchar(8000) NULL, 
	[ContractAmount] decimal(18,2) NULL, 
	[ContractCurrencyId] int NULL, 
	[ContractProductId] int NULL, 
	[ContractStatusId] int NULL, 
	[ContractorId] int NULL, 
	[ExternalTenderId] varchar(255) NULL
);


GO
ALTER TABLE [tender].[AwardContract] ADD CONSTRAINT PK_AwardContract primary key NONCLUSTERED ([AwardContractId]);
GO
ALTER TABLE [tender].[AwardContract] ADD CONSTRAINT FK_AwardContract_AwardedId FOREIGN KEY ([AwardedId]) REFERENCES [company].[Company]([CompanyId]);
GO
ALTER TABLE [tender].[AwardContract] ADD CONSTRAINT FK_AwardContract_BuyerId FOREIGN KEY ([BuyerId]) REFERENCES [company].[Company]([CompanyId]);
GO
ALTER TABLE [tender].[AwardContract] ADD CONSTRAINT FK_AwardContract_ContractCurrencyId FOREIGN KEY ([ContractCurrencyId]) REFERENCES [list].[Currency]([CurrencyId]);
GO
ALTER TABLE [tender].[AwardContract] ADD CONSTRAINT FK_AwardContract_ContractProductId FOREIGN KEY ([ContractProductId]) REFERENCES [tender].[Product]([ProductId]);
GO
ALTER TABLE [tender].[AwardContract] ADD CONSTRAINT FK_AwardContract_ContractStatusId FOREIGN KEY ([ContractStatusId]) REFERENCES [tender].[TenderStatus]([TenderStatusId]);
GO
ALTER TABLE [tender].[AwardContract] ADD CONSTRAINT FK_AwardContract_ContractorId FOREIGN KEY ([ContractorId]) REFERENCES [company].[Company]([CompanyId]);
GO
ALTER TABLE [tender].[AwardContract] ADD CONSTRAINT FK_AwardContract_CurrencyId FOREIGN KEY ([CurrencyId]) REFERENCES [list].[Currency]([CurrencyId]);
GO
ALTER TABLE [tender].[AwardContract] ADD CONSTRAINT FK_AwardContract_ProductId FOREIGN KEY ([ProductId]) REFERENCES [tender].[Product]([ProductId]);
GO
ALTER TABLE [tender].[AwardContract] ADD CONSTRAINT FK_AwardContract_TenderId FOREIGN KEY ([TenderId]) REFERENCES [tender].[Tenders]([TenderId]);
GO
ALTER TABLE [tender].[AwardContract] ADD CONSTRAINT FK_AwardContract_TenderStatusId FOREIGN KEY ([TenderStatusId]) REFERENCES [tender].[TenderStatus]([TenderStatusId]);
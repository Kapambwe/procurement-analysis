CREATE TABLE [tender].[TenderItems] (

	[TenderItemId] varchar(50) NOT NULL, 
	[ExternalTenderId] varchar(50) NOT NULL, 
	[ProductId] int NOT NULL, 
	[Quantity] decimal(18,2) NOT NULL, 
	[UnitName] varchar(50) NOT NULL, 
	[ExternalItemId] varchar(50) NOT NULL, 
	[BuyerId] int NOT NULL, 
	[TenderDate] datetime2(6) NULL, 
	[TenderAmount] decimal(18,2) NULL, 
	[TenderId] int NULL
);


GO
ALTER TABLE [tender].[TenderItems] ADD CONSTRAINT PK_TenderItems primary key NONCLUSTERED ([TenderItemId]);
GO
ALTER TABLE [tender].[TenderItems] ADD CONSTRAINT FK_TenderItems_Buyer FOREIGN KEY ([BuyerId]) REFERENCES [company].[Company]([CompanyId]);
GO
ALTER TABLE [tender].[TenderItems] ADD CONSTRAINT FK_TenderItems_Product FOREIGN KEY ([ProductId]) REFERENCES [tender].[Product]([ProductId]);
GO
ALTER TABLE [tender].[TenderItems] ADD CONSTRAINT FK_TenderItems_Tenders FOREIGN KEY ([TenderId]) REFERENCES [tender].[Tenders]([TenderId]);
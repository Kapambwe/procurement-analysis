CREATE TABLE [tender].[Product] (

	[ProductId] int NOT NULL, 
	[Name] varchar(1000) NULL, 
	[Description] varchar(4000) NULL, 
	[Classification] varchar(1000) NULL, 
	[Scheme] varchar(1000) NULL, 
	[ExternalId] varchar(100) NULL, 
	[Uri] varchar(1000) NULL
);


GO
ALTER TABLE [tender].[Product] ADD CONSTRAINT PK_Product primary key NONCLUSTERED ([ProductId]);
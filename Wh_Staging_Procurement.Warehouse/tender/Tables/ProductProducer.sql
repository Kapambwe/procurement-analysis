CREATE TABLE [tender].[ProductProducer] (

	[ProductProducerId] int NOT NULL, 
	[CompanyId] int NOT NULL, 
	[ProductId] int NOT NULL
);


GO
ALTER TABLE [tender].[ProductProducer] ADD CONSTRAINT PK_ProductProducer primary key NONCLUSTERED ([ProductProducerId]);
CREATE TABLE [list].[Currency] (

	[CurrencyId] int NOT NULL, 
	[Name] varchar(50) NOT NULL
);


GO
ALTER TABLE [list].[Currency] ADD CONSTRAINT PK_Currency primary key NONCLUSTERED ([CurrencyId]);
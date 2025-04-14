CREATE TABLE [list].[Country] (

	[CountryId] int NOT NULL, 
	[Name] varchar(50) NOT NULL, 
	[ShortName] varchar(50) NULL, 
	[SymbolCountry] varchar(50) NULL, 
	[Symbol] varchar(10) NULL, 
	[CurrencySymbol] varchar(30) NULL, 
	[TimeZone] varchar(30) NULL, 
	[TimeToUtc] decimal(18,0) NULL, 
	[ContinentId] int NOT NULL, 
	[RegionAreaId] int NULL
);


GO
ALTER TABLE [list].[Country] ADD CONSTRAINT PK_Country primary key NONCLUSTERED ([CountryId]);
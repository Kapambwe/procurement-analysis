CREATE TABLE [list].[CountryRegion] (

	[CountryRegionId] int NOT NULL, 
	[Name] varchar(100) NOT NULL, 
	[CountryRegionTypeId] int NOT NULL, 
	[ParentCountryRegionId] int NULL, 
	[CountryRegion] varchar(100) NULL, 
	[CountryId] int NULL
);


GO
ALTER TABLE [list].[CountryRegion] ADD CONSTRAINT PK_CountryRegion primary key NONCLUSTERED ([CountryRegionId]);
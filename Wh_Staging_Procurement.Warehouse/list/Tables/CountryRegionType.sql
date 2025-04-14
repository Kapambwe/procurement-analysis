CREATE TABLE [list].[CountryRegionType] (

	[CountryRegionTypeId] int NOT NULL, 
	[Name] varchar(100) NOT NULL
);


GO
ALTER TABLE [list].[CountryRegionType] ADD CONSTRAINT PK_CountryRegionType primary key NONCLUSTERED ([CountryRegionTypeId]);
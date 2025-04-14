CREATE TABLE [list].[Continent] (

	[ContinentId] int NOT NULL, 
	[Name] varchar(50) NOT NULL
);


GO
ALTER TABLE [list].[Continent] ADD CONSTRAINT PK_Continent primary key NONCLUSTERED ([ContinentId]);
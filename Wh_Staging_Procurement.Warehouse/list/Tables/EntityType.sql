CREATE TABLE [list].[EntityType] (

	[EntityTypeId] int NOT NULL, 
	[Name] varchar(4000) NULL
);


GO
ALTER TABLE [list].[EntityType] ADD CONSTRAINT PK_EntityType primary key NONCLUSTERED ([EntityTypeId]);
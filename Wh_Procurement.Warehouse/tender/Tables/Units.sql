CREATE TABLE [tender].[Units] (

	[UnitsId] int NOT NULL, 
	[Name] varchar(50) NOT NULL
);


GO
ALTER TABLE [tender].[Units] ADD CONSTRAINT PK_Units primary key NONCLUSTERED ([UnitsId]);
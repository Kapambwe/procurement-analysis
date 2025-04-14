CREATE TABLE [list].[BusinessType] (

	[BusinessTypeId] int NOT NULL, 
	[Name] varchar(4000) NOT NULL, 
	[Symbol] varchar(10) NULL
);


GO
ALTER TABLE [list].[BusinessType] ADD CONSTRAINT PK_BusinessType primary key NONCLUSTERED ([BusinessTypeId]);
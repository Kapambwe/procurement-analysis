CREATE TABLE [tender].[PersonRole] (

	[PersonRoleId] int NOT NULL, 
	[Name] varchar(100) NULL
);


GO
ALTER TABLE [tender].[PersonRole] ADD CONSTRAINT PK_PersonRole primary key NONCLUSTERED ([PersonRoleId]);
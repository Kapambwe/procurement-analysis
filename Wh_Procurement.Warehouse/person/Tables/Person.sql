CREATE TABLE [person].[Person] (

	[PersonId] int NOT NULL, 
	[FirstName] varchar(100) NOT NULL, 
	[LastName] varchar(100) NULL, 
	[Gender] varchar(10) NULL, 
	[BirthDate] datetime2(6) NULL
);


GO
ALTER TABLE [person].[Person] ADD CONSTRAINT PK_Person primary key NONCLUSTERED ([PersonId]);
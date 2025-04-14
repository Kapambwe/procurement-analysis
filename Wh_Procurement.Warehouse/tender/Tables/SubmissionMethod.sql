CREATE TABLE [tender].[SubmissionMethod] (

	[SubmissionMethodId] int NOT NULL, 
	[Name] varchar(200) NOT NULL, 
	[Description] varchar(1000) NULL
);


GO
ALTER TABLE [tender].[SubmissionMethod] ADD CONSTRAINT PK_SubmissionMethod primary key NONCLUSTERED ([SubmissionMethodId]);
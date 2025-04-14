CREATE TABLE [tender].[SubmissionMethodDetail] (

	[SubmissionMethodDetailId] int NOT NULL, 
	[Name] varchar(1000) NULL, 
	[Description] varchar(4000) NULL
);


GO
ALTER TABLE [tender].[SubmissionMethodDetail] ADD CONSTRAINT PK_SubmissionMethodDetail primary key NONCLUSTERED ([SubmissionMethodDetailId]);
CREATE TABLE [tender].[AwardCriteriaDetail] (

	[AwardCriteriaDetailId] int NOT NULL, 
	[Name] varchar(8000) NULL, 
	[Description] varchar(8000) NULL
);


GO
ALTER TABLE [tender].[AwardCriteriaDetail] ADD CONSTRAINT PK_AwardCriteriaDetail primary key NONCLUSTERED ([AwardCriteriaDetailId]);
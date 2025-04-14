CREATE TABLE [tender].[AwardCriteria] (

	[AwardCriteriaId] int NOT NULL, 
	[Name] varchar(200) NOT NULL, 
	[Description] varchar(1000) NULL
);


GO
ALTER TABLE [tender].[AwardCriteria] ADD CONSTRAINT PK_AwardCriteria primary key NONCLUSTERED ([AwardCriteriaId]);
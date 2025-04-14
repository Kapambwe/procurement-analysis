CREATE TABLE [tender].[EligibilityCriteria] (

	[EligibilityCriteriaId] int NOT NULL, 
	[Name] varchar(8000) NULL, 
	[Description] varchar(8000) NULL
);


GO
ALTER TABLE [tender].[EligibilityCriteria] ADD CONSTRAINT PK_EligibilityCriteria primary key NONCLUSTERED ([EligibilityCriteriaId]);
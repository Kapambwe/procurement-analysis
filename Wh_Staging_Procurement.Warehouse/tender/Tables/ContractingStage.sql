CREATE TABLE [tender].[ContractingStage] (

	[ContractingStageId] int NOT NULL, 
	[Name] varchar(50) NOT NULL
);


GO
ALTER TABLE [tender].[ContractingStage] ADD CONSTRAINT PK_ContractingStage primary key NONCLUSTERED ([ContractingStageId]);
CREATE TABLE [tender].[ContractImplementation] (

	[ContractImplementationId] int NOT NULL, 
	[ContractTenderId] int NULL
);


GO
ALTER TABLE [tender].[ContractImplementation] ADD CONSTRAINT PK_ContractImplementation primary key NONCLUSTERED ([ContractImplementationId]);
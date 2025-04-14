CREATE TABLE [tender].[ContractingProcessPartyRole] (

	[ContractingProcessPartyRoleId] int NOT NULL, 
	[ContractingProcessId] int NOT NULL, 
	[ContractingPartyRoleId] int NOT NULL, 
	[CompanyId] int NOT NULL
);


GO
ALTER TABLE [tender].[ContractingProcessPartyRole] ADD CONSTRAINT PK_ContractingProcessPartyRole primary key NONCLUSTERED ([ContractingProcessPartyRoleId]);
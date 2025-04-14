CREATE TABLE [tender].[RedFlag] (

	[RedFlagId] int NOT NULL, 
	[ID] varchar(50) NULL, 
	[Stage] varchar(50) NOT NULL, 
	[Associated_Scheme_s] varchar(150) NULL, 
	[Red_Flag] varchar(150) NOT NULL, 
	[Indicator_Description] varchar(300) NOT NULL, 
	[Calculation_method] varchar(800) NOT NULL, 
	[Rationale] varchar(1150) NOT NULL, 
	[OCDS_fields] varchar(500) NOT NULL, 
	[Aditional_data_fields] varchar(100) NULL, 
	[OCDS_Extensions] varchar(50) NULL, 
	[Description_of_fields] varchar(300) NOT NULL, 
	[Source_Evidence] varchar(150) NULL
);


GO
ALTER TABLE [tender].[RedFlag] ADD CONSTRAINT PK_RedFlag primary key NONCLUSTERED ([RedFlagId]);
CREATE TABLE [tender].[AwardTender] (

	[AwardTenderId] int NOT NULL, 
	[Name] varchar(200) NOT NULL, 
	[Description] varchar(4000) NULL, 
	[AwardStatus] varchar(200) NOT NULL, 
	[AwardDate] datetime2(6) NOT NULL, 
	[AwardAmount] decimal(18,2) NULL
);
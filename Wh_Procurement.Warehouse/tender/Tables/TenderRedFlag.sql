CREATE TABLE [tender].[TenderRedFlag] (

	[TenderRedFlagId] int NOT NULL, 
	[RedFlagId] int NOT NULL, 
	[TenderId] int NOT NULL, 
	[TrackDateTime] date NULL, 
	[Value] varchar(max) NULL, 
	[ValueType] varchar(50) NULL
);


GO
ALTER TABLE [tender].[TenderRedFlag] ADD CONSTRAINT PK_TenderRedFlag primary key NONCLUSTERED ([TenderRedFlagId]);
GO
ALTER TABLE [tender].[TenderRedFlag] ADD CONSTRAINT FK_TenderRedFlag_RedFlagId FOREIGN KEY ([RedFlagId]) REFERENCES [tender].[RedFlag]([RedFlagId]);
GO
ALTER TABLE [tender].[TenderRedFlag] ADD CONSTRAINT FK_TenderRedFlag_TenderId FOREIGN KEY ([TenderId]) REFERENCES [tender].[Tender]([TenderId]);
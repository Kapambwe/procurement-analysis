CREATE TABLE [tender].[CorruptionRiskScore] (

	[CorruptionRiskScoreId] int NOT NULL, 
	[TenderRedFlagId] int NOT NULL, 
	[TrackDateTime] date NULL, 
	[Value] int NOT NULL
);


GO
ALTER TABLE [tender].[CorruptionRiskScore] ADD CONSTRAINT PK_CorruptionRiskScore primary key NONCLUSTERED ([CorruptionRiskScoreId]);
GO
ALTER TABLE [tender].[CorruptionRiskScore] ADD CONSTRAINT FK_CorruptionRiskScore_TenderRedFlagId FOREIGN KEY ([TenderRedFlagId]) REFERENCES [tender].[TenderRedFlag]([TenderRedFlagId]);
CREATE TABLE [tender].[TenderCorruptionIndex] (

	[TenderCorruptionIndexId] int NOT NULL, 
	[TenderId] int NOT NULL, 
	[CorruptionIndexScore] decimal(10,2) NOT NULL, 
	[TrackDateTime] date NOT NULL
);


GO
ALTER TABLE [tender].[TenderCorruptionIndex] ADD CONSTRAINT PK_TenderCorruptionIndex primary key NONCLUSTERED ([TenderCorruptionIndexId]);
GO
ALTER TABLE [tender].[TenderCorruptionIndex] ADD CONSTRAINT FK_TenderId FOREIGN KEY ([TenderId]) REFERENCES [tender].[Tender]([TenderId]);
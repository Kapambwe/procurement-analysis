CREATE TABLE [meta].[WhProcurement_Metadata] (

	[TargetSchema] varchar(25) NULL, 
	[TargetTable] varchar(100) NULL, 
	[SourceSchema] varchar(25) NULL, 
	[SourceTable] varchar(100) NULL, 
	[StagingSchema] varchar(25) NULL, 
	[StagingTable] varchar(100) NULL, 
	[StagingDatabase] varchar(100) NULL, 
	[LoadType] varchar(25) NULL, 
	[LoadIndicator] varchar(25) NULL, 
	[ETLStrategy] varchar(50) NULL, 
	[SourceStoredProcedureName] varchar(500) NULL, 
	[TargetStoredProcedureName] varchar(500) NULL, 
	[ColumnKey] varchar(500) NULL, 
	[NumberOfPrimaryKeyColumns] smallint NULL, 
	[WaterfallColumn] varchar(100) NULL, 
	[TableColumns] varchar(1000) NULL, 
	[ExecutionOrder] int NULL
);
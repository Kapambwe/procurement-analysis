CREATE TABLE [audit].[PipelineRun] (

	[PipelineRunId] varchar(100) NOT NULL, 
	[PipelineId] varchar(100) NULL, 
	[StartTimeUTC] datetime2(6) NULL, 
	[EndTimeUTC] datetime2(6) NULL, 
	[WorkspaceId] varchar(100) NULL, 
	[PipelineTriggerId] varchar(100) NULL, 
	[ParentPipelineRunId] varchar(100) NULL, 
	[PipelineCompletedSuccessfully] int NULL, 
	[Process] varchar(500) NULL
);
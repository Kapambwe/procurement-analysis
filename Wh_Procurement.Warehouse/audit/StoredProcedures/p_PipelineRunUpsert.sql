CREATE PROCEDURE [audit].[p_PipelineRunUpsert]
    @PipelineRunId varchar(100),
    @PipelineId varchar(100) = NULL,
    @StartTimeUTC DATETIME2(6) = NULL,
    @EndTimeUTC DATETIME2(6) = NULL,
    @WorkspaceId varchar(100) = NULL,
    @PipelineTriggerId varchar(100) = NULL,
    @ParentPipelineRunId varchar(100) = NULL,
    @PipelineCompletedSuccessfully int = NULL,
    @Process varchar(500) = NULL
AS
BEGIN
    SET NOCOUNT ON;

    IF NOT EXISTS (SELECT * FROM audit.PipelineRun WHERE PipelineRunId = @PipelineRunId)
    BEGIN
        INSERT INTO audit.PipelineRun
        (
            PipelineRunId, PipelineId, StartTimeUTC, EndTimeUTC, WorkspaceId, 
            PipelineTriggerId, ParentPipelineRunId, PipelineCompletedSuccessfully, Process
        )
        VALUES 
        (
            @PipelineRunId, @PipelineId, @StartTimeUTC, @EndTimeUTC, @WorkspaceId, 
            @PipelineTriggerId, @ParentPipelineRunId, @PipelineCompletedSuccessfully, @Process
        )
    END
    ELSE
    BEGIN
        UPDATE audit.PipelineRun
        SET 
            PipelineId = ISNULL(@PipelineId, PipelineId),
            StartTimeUTC = ISNULL(@StartTimeUTC, StartTimeUTC),
            EndTimeUTC = ISNULL(@EndTimeUTC, EndTimeUTC),
            WorkspaceId = ISNULL(@WorkspaceId, WorkspaceId),
            PipelineTriggerId = ISNULL(@PipelineTriggerId, PipelineTriggerId),
            ParentPipelineRunId = ISNULL(@ParentPipelineRunId, ParentPipelineRunId),
            PipelineCompletedSuccessfully = ISNULL(@PipelineCompletedSuccessfully, PipelineCompletedSuccessfully),
            Process = ISNULL(@Process, Process)
        WHERE PipelineRunId = @PipelineRunId
    END
END
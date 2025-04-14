-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
CREATE PROCEDURE [tender].[UpdateOrInsertIntoSubmissionMethodDetail]
AS
BEGIN
    -- SET NOCOUNT ON added to prevent extra result sets from
    -- interfering with SELECT statements.
    SET NOCOUNT ON;

    -- Update existing records
    UPDATE target
    SET
        target.[Name] = source.[Name],
        target.[Description] = source.[Description]
    FROM [tender].[SubmissionMethodDetail] AS target
    INNER JOIN [Wh_Staging_Procurement].[tender].[SubmissionMethodDetail] AS source
    ON target.[SubmissionMethodDetailId] = source.[SubmissionMethodDetailId];

    -- Insert new records
    INSERT INTO [tender].[SubmissionMethodDetail] ([SubmissionMethodDetailId], [Name], [Description])
    SELECT 
        source.[SubmissionMethodDetailId], 
        source.[Name], 
        source.[Description]
    FROM [Wh_Staging_Procurement].[tender].[SubmissionMethodDetail] AS source
    LEFT JOIN [tender].[SubmissionMethodDetail] AS target
    ON source.[SubmissionMethodDetailId] = target.[SubmissionMethodDetailId]
    WHERE target.[SubmissionMethodDetailId] IS NULL;

END;
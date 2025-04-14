-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
CREATE PROCEDURE [tender].[UpdateOrInsertIntoSubmissionMethod]
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
    FROM [tender].[SubmissionMethod] AS target
    INNER JOIN [Wh_Staging_Procurement].[tender].[SubmissionMethod] AS source
    ON target.[SubmissionMethodId] = source.[SubmissionMethodId];

    -- Insert new records
    INSERT INTO [tender].[SubmissionMethod] ([SubmissionMethodId], [Name], [Description])
    SELECT 
        source.[SubmissionMethodId], 
        source.[Name], 
        source.[Description]
    FROM [Wh_Staging_Procurement].[tender].[SubmissionMethod] AS source
    LEFT JOIN [tender].[SubmissionMethod] AS target
    ON source.[SubmissionMethodId] = target.[SubmissionMethodId]
    WHERE target.[SubmissionMethodId] IS NULL;

END;
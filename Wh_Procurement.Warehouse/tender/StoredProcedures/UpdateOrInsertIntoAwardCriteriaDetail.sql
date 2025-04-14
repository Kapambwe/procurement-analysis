-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
CREATE PROCEDURE [tender].[UpdateOrInsertIntoAwardCriteriaDetail]
AS
BEGIN
    -- SET NOCOUNT ON added to prevent extra result sets from
    -- interfering with SELECT statements.
    SET NOCOUNT ON;

    DECLARE @MaxLength INT = 8000;

    -- Update existing records
    UPDATE target
    SET
        target.[Name] = source.[Name],
        target.[Description] = source.[Description]
        -- Add more columns as needed
    FROM [tender].[AwardCriteriaDetail] AS target
    INNER JOIN (
        SELECT 
            acd.Description AS [Description],
            AwardCriteriaDetailId,
            acd.Name AS [Name]
        FROM [Wh_Staging_Procurement].[tender].[AwardCriteriaDetail] acd
    ) AS source
    ON target.[AwardCriteriaDetailId] = source.[AwardCriteriaDetailId];

    -- Insert new records
    INSERT INTO [tender].[AwardCriteriaDetail] ([AwardCriteriaDetailId], [Name], [Description])
    SELECT source.[AwardCriteriaDetailId], source.[Name], source.[Description]
    FROM (
        SELECT 
            acd.Description AS [Description],
            AwardCriteriaDetailId,
            acd.Name AS [Name]
        FROM [Wh_Staging_Procurement].[tender].[AwardCriteriaDetail] acd
    ) AS source
    LEFT JOIN [tender].[AwardCriteriaDetail] AS target
    ON source.[AwardCriteriaDetailId] = target.[AwardCriteriaDetailId]
    WHERE target.[AwardCriteriaDetailId] IS NULL;

END;
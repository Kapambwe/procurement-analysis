-- =============================================
-- Author:		Abraham Kapambwe
-- Create date: 20-07-2024
-- Description:	Insert 
-- =============================================
CREATE PROCEDURE [tender].[UpdateOrInsertIntoAwardCriteria]
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
        -- Add more columns as needed
    FROM [tender].[AwardCriteria] AS target
    INNER JOIN [Wh_Staging_Procurement].[list].[AwardCriteria] AS source
    ON target.[AwardCriteriaId] = source.[AwardCriteriaId];

    -- Insert new records
    INSERT INTO [tender].[AwardCriteria] ([AwardCriteriaId], [Name], [Description])
    SELECT source.[AwardCriteriaId], source.[Name], source.[Description]
    FROM [Wh_Staging_Procurement].[list].[AwardCriteria] AS source
    LEFT JOIN [tender].[AwardCriteria] AS target
    ON source.[AwardCriteriaId] = target.[AwardCriteriaId]
    WHERE target.[AwardCriteriaId] IS NULL;

END;
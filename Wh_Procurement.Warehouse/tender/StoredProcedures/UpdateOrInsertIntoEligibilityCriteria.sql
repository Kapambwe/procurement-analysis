-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
CREATE PROCEDURE [tender].[UpdateOrInsertIntoEligibilityCriteria]
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
    FROM [tender].[EligibilityCriteria] AS target
    INNER JOIN (
        SELECT 
            ec.Description AS [Description],
            ec.EligibilityCriteriaId,
            ec.Name AS [Name]
        FROM [Wh_Staging_Procurement].[tender].[EligibilityCriteria] ec
    ) AS source
    ON target.[EligibilityCriteriaId] = source.[EligibilityCriteriaId];

    -- Insert new records
    INSERT INTO [tender].[EligibilityCriteria] ([EligibilityCriteriaId], [Name], [Description])
    SELECT 
        source.[EligibilityCriteriaId], 
        source.[Name], 
        source.[Description]
    FROM (
        SELECT 
            ec.Description AS [Description],
            ec.EligibilityCriteriaId,
            ec.Name AS [Name]
        FROM [Wh_Staging_Procurement].[tender].[EligibilityCriteria] ec
    ) AS source
    LEFT JOIN [tender].[EligibilityCriteria] AS target
    ON source.[EligibilityCriteriaId] = target.[EligibilityCriteriaId]
    WHERE target.[EligibilityCriteriaId] IS NULL;

END;
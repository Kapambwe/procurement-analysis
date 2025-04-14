-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
CREATE PROCEDURE [tender].[UpdateOrInsertIntoProcurementMethodRationale]
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
    FROM [tender].[ProcurementMethodRationale] AS target
    INNER JOIN (
        SELECT 
            acd.Description AS [Description],
            acd.ProcurementMethodRationaleId,
            acd.Name AS [Name]
        FROM [Wh_Staging_Procurement].[tender].[ProcurementMethodRationale] acd
    ) AS source
    ON target.[ProcurementMethodRationaleId] = source.[ProcurementMethodRationaleId];

    -- Insert new records
    INSERT INTO [tender].[ProcurementMethodRationale] ([ProcurementMethodRationaleId], [Name], [Description])
    SELECT 
        source.[ProcurementMethodRationaleId], 
        source.[Name], 
        source.[Description]
    FROM (
        SELECT 
            acd.Description AS [Description],
            acd.ProcurementMethodRationaleId,
            acd.Name AS [Name]
        FROM [Wh_Staging_Procurement].[tender].[ProcurementMethodRationale] acd
    ) AS source
    LEFT JOIN [tender].[ProcurementMethodRationale] AS target
    ON source.[ProcurementMethodRationaleId] = target.[ProcurementMethodRationaleId]
    WHERE target.[ProcurementMethodRationaleId] IS NULL;

END;
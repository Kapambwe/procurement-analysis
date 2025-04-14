-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
CREATE PROCEDURE [tender].[UpdateOrInsertIntoProcurementMethod]
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
    FROM [tender].[ProcurementMethod] AS target
    INNER JOIN [Wh_Staging_Procurement].[tender].[ProcurementMethod] AS source
    ON target.[ProcurementMethodId] = source.[ProcurementMethodId];

    -- Insert new records
    INSERT INTO [tender].[ProcurementMethod] ([ProcurementMethodId], [Name], [Description])
    SELECT source.[ProcurementMethodId], source.[Name], source.[Description]
    FROM [Wh_Staging_Procurement].[tender].[ProcurementMethod] AS source
    LEFT JOIN [tender].[ProcurementMethod] AS target
    ON source.[ProcurementMethodId] = target.[ProcurementMethodId]
    WHERE target.[ProcurementMethodId] IS NULL;

END;
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
CREATE PROCEDURE [tender].[UpdateOrInsertIntoTenderStatus]
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
    FROM [tender].[TenderStatus] AS target
    INNER JOIN [Wh_Staging_Procurement].[tender].[TenderStatus] AS source
    ON target.[TenderStatusId] = source.[TenderStatusId];

    -- Insert new records
    INSERT INTO [tender].[TenderStatus] ([TenderStatusId], [Name], [Description])
    SELECT 
        source.[TenderStatusId], 
        source.[Name], 
        source.[Description]
    FROM [Wh_Staging_Procurement].[tender].[TenderStatus] AS source
    LEFT JOIN [tender].[TenderStatus] AS target
    ON source.[TenderStatusId] = target.[TenderStatusId]
    WHERE target.[TenderStatusId] IS NULL;

END;
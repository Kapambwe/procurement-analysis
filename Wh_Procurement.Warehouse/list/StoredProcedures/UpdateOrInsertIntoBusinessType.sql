-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
CREATE PROCEDURE [list].[UpdateOrInsertIntoBusinessType]
AS
BEGIN
    -- SET NOCOUNT ON added to prevent extra result sets from
    -- interfering with SELECT statements.
    SET NOCOUNT ON;

    -- Update existing records
    UPDATE target
    SET
        target.[Name] = source.[Name],
        target.[Symbol] = source.[Symbol]
    FROM [list].[BusinessType] AS target
    INNER JOIN [Wh_Staging_Procurement].[list].[BusinessType] AS source
    ON target.[BusinessTypeId] = source.[BusinessTypeId];

    -- Insert new records
    INSERT INTO [list].[BusinessType] ([BusinessTypeId], [Name], [Symbol])
    SELECT source.[BusinessTypeId], source.[Name], source.[Symbol]
    FROM [Wh_Staging_Procurement].[list].[BusinessType] AS source
    LEFT JOIN [list].[BusinessType] AS target
    ON source.[BusinessTypeId] = target.[BusinessTypeId]
    WHERE target.[BusinessTypeId] IS NULL;

END;
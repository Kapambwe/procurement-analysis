-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
CREATE PROCEDURE [list].[UpdateOrInsertIntoCurrency]
AS
BEGIN
    -- SET NOCOUNT ON added to prevent extra result sets from
    -- interfering with SELECT statements.
    SET NOCOUNT ON;

    -- Update existing records
    UPDATE target
    SET
        target.[Name] = source.[Name]
    FROM [list].[Currency] AS target
    INNER JOIN [Wh_Staging_Procurement].[list].[Currency] AS source
    ON target.[CurrencyId] = source.[CurrencyId];

    -- Insert new records
    INSERT INTO [list].[Currency] ([CurrencyId], [Name])
    SELECT source.[CurrencyId], source.[Name]
    FROM [Wh_Staging_Procurement].[list].[Currency] AS source
    LEFT JOIN [list].[Currency] AS target
    ON source.[CurrencyId] = target.[CurrencyId]
    WHERE target.[CurrencyId] IS NULL;

END;
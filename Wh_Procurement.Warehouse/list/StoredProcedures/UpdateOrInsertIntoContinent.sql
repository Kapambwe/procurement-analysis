-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
CREATE PROCEDURE [list].[UpdateOrInsertIntoContinent]
AS
BEGIN
    -- SET NOCOUNT ON added to prevent extra result sets from
    -- interfering with SELECT statements.
    SET NOCOUNT ON;

    -- Update existing records
    UPDATE target
    SET
        target.[Name] = source.[Name]
    FROM [list].[Continent] AS target
    INNER JOIN [Wh_Staging_Procurement].[list].[Continent] AS source
    ON target.[ContinentId] = source.[ContinentId];

    -- Insert new records
    INSERT INTO [list].[Continent] ([ContinentId], [Name])
    SELECT source.[ContinentId], source.[Name]
    FROM [Wh_Staging_Procurement].[list].[Continent] AS source
    LEFT JOIN [list].[Continent] AS target
    ON source.[ContinentId] = target.[ContinentId]
    WHERE target.[ContinentId] IS NULL;

END;
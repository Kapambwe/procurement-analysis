-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
CREATE PROCEDURE [list].[UpdateOrInsertIntoCountry]
AS
BEGIN
    -- SET NOCOUNT ON added to prevent extra result sets from
    -- interfering with SELECT statements.
    SET NOCOUNT ON;

    -- Update existing records
    UPDATE target
    SET
        target.[Name] = source.[Name],
        target.[ShortName] = source.[ShortName],
        target.[SymbolCountry] = source.[SymbolCountry],
        target.[Symbol] = source.[Symbol],
        target.[CurrencySymbol] = source.[CurrencySymbol],
        target.[TimeZone] = source.[TimeZone],
        target.[TimeToUtc] = source.[TimeToUtc],
        target.[ContinentId] = source.[ContinentId],
        target.[RegionAreaId] = source.[RegionAreaId]
    FROM [list].[Country] AS target
    INNER JOIN [Wh_Staging_Procurement].[list].[Country] AS source
    ON target.[CountryId] = source.[CountryId];

    -- Insert new records
    INSERT INTO [list].[Country] ([CountryId], [Name], [ShortName], [SymbolCountry], [Symbol], [CurrencySymbol], [TimeZone], [TimeToUtc], [ContinentId], [RegionAreaId])
    SELECT source.[CountryId], source.[Name], source.[ShortName], source.[SymbolCountry], source.[Symbol], source.[CurrencySymbol], source.[TimeZone], source.[TimeToUtc], source.[ContinentId], source.[RegionAreaId]
    FROM [Wh_Staging_Procurement].[list].[Country] AS source
    LEFT JOIN [list].[Country] AS target
    ON source.[CountryId] = target.[CountryId]
    WHERE target.[CountryId] IS NULL;

END;
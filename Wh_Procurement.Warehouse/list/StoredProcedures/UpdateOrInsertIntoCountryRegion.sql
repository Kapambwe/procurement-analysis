-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
CREATE PROCEDURE [list].[UpdateOrInsertIntoCountryRegion]
AS
BEGIN
    -- SET NOCOUNT ON added to prevent extra result sets from
    -- interfering with SELECT statements.
    SET NOCOUNT ON;

    -- Update existing records
    UPDATE target
    SET
        target.[Name] = source.[Name],
        target.[CountryRegionTypeId] = source.[CountryRegionTypeId],
        target.[ParentCountryRegionId] = source.[ParentCountryRegionId],
        target.[CountryId] = source.[CountryId]
    FROM [list].[CountryRegion] AS target
    INNER JOIN [Wh_Staging_Procurement].[list].[CountryRegion] AS source
    ON target.[CountryRegionId] = source.[CountryRegionId];

    -- Insert new records
    INSERT INTO [list].[CountryRegion] ([CountryRegionId], [Name], [CountryRegionTypeId], [ParentCountryRegionId], [CountryId])
    SELECT source.[CountryRegionId], source.[Name], source.[CountryRegionTypeId], source.[ParentCountryRegionId], source.[CountryId]
    FROM [Wh_Staging_Procurement].[list].[CountryRegion] AS source
    LEFT JOIN [list].[CountryRegion] AS target
    ON source.[CountryRegionId] = target.[CountryRegionId]
    WHERE target.[CountryRegionId] IS NULL;

END;
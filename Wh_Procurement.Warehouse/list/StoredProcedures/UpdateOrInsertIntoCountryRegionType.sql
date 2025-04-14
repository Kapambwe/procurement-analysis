-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
CREATE PROCEDURE [list].[UpdateOrInsertIntoCountryRegionType]
AS
BEGIN
    -- SET NOCOUNT ON added to prevent extra result sets from
    -- interfering with SELECT statements.
    SET NOCOUNT ON;

    -- Update existing records
    UPDATE target
    SET
        target.[Name] = source.[Name]
    FROM [list].[CountryRegionType] AS target
    INNER JOIN [Wh_Staging_Procurement].[list].[CountryRegionType] AS source
    ON target.[CountryRegionTypeId] = source.[CountryRegionTypeId];

    -- Insert new records
    INSERT INTO [list].[CountryRegionType] ([CountryRegionTypeId], [Name])
    SELECT source.[CountryRegionTypeId], source.[Name]
    FROM [Wh_Staging_Procurement].[list].[CountryRegionType] AS source
    LEFT JOIN [list].[CountryRegionType] AS target
    ON source.[CountryRegionTypeId] = target.[CountryRegionTypeId]
    WHERE target.[CountryRegionTypeId] IS NULL;

END;
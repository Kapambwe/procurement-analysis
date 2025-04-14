-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
CREATE PROCEDURE [tender].[UpdateOrInsertIntoCompanyRole]
AS
BEGIN
    -- SET NOCOUNT ON added to prevent extra result sets from
    -- interfering with SELECT statements.
    SET NOCOUNT ON;

    -- Update existing records
    UPDATE target
    SET
        target.[Name] = source.[Name],
        target.[Description] = source.[Description],
        target.[Code] = source.[Code],
        target.[RelationShipName] = source.[RelationShipName]
    FROM [tender].[CompanyRole] AS target
    INNER JOIN [Wh_Staging_Procurement].[list].[CompanyPartyRole] AS source
    ON target.[CompanyRoleId] = source.[CompanyPartyRoleId];

    -- Insert new records
    INSERT INTO [tender].[CompanyRole] ([CompanyRoleId], [Name], [Description], [Code], [RelationShipName])
    SELECT source.[CompanyPartyRoleId], source.[Name], source.[Description], source.[Code], source.[RelationShipName]
    FROM [Wh_Staging_Procurement].[list].[CompanyPartyRole] AS source
    LEFT JOIN [tender].[CompanyRole] AS target
    ON source.[CompanyPartyRoleId] = target.[CompanyRoleId]
    WHERE target.[CompanyRoleId] IS NULL;

END;
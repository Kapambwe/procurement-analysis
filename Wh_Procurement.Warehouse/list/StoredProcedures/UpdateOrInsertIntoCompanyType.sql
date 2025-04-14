-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
CREATE PROCEDURE [list].[UpdateOrInsertIntoCompanyType]
AS
BEGIN
    -- SET NOCOUNT ON added to prevent extra result sets from
    -- interfering with SELECT statements.
    SET NOCOUNT ON;

    -- Update existing records
    UPDATE target
    SET
        target.[Name] = source.[Name],
        target.[IsActive] = source.[IsActive]
    FROM [list].[CompanyType] AS target
    INNER JOIN [Wh_Staging_Procurement].[list].[CompanyType] AS source
    ON target.[CompanyTypeId] = source.[CompanyTypeId];

    -- Insert new records
    INSERT INTO [list].[CompanyType] ([CompanyTypeId], [Name], [IsActive])
    SELECT source.[CompanyTypeId], source.[Name], source.[IsActive]
    FROM [Wh_Staging_Procurement].[list].[CompanyType] AS source
    LEFT JOIN [list].[CompanyType] AS target
    ON source.[CompanyTypeId] = target.[CompanyTypeId]
    WHERE target.[CompanyTypeId] IS NULL;

END;
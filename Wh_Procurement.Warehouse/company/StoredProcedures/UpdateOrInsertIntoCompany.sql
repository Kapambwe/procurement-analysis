CREATE PROCEDURE [company].[UpdateOrInsertIntoCompany]
AS
BEGIN
    -- SET NOCOUNT ON added to prevent extra result sets from
    -- interfering with SELECT statements.
    SET NOCOUNT ON;

    -- Update existing records
    UPDATE target
    SET
        target.[Name] = source.[Name],
        target.[CountryId] = source.[CountryId],
        target.[BusinessTypeId] = source.[BusinessTypeId],
        target.[CompanyTypeId] = source.[CompanyTypeId],
        target.[Address] = source.[Address],
        target.[Active] = source.[Active],
        target.[PhoneNumber] = source.[PhoneNumber],
        target.[EmailAddress] = source.[EmailAddress],
        target.[City] = source.[City],
        target.[LegalName] = source.[LegalName],
        target.[PostalCode] = source.[PostalCode],
        target.[ParentCompanyId] = source.[ParentCompanyId]
    FROM [company].[Company] AS target
    INNER JOIN [Wh_Staging_Procurement].[company].[Company] AS source
    ON target.[CompanyId] = source.[CompanyId];

    -- Insert new records
    INSERT INTO [company].[Company] ([CompanyId], [Name], [CountryId], [BusinessTypeId], [CompanyTypeId], [Address], [Active], [PhoneNumber], [EmailAddress], [City], [LegalName], [PostalCode], [ParentCompanyId])
    SELECT source.[CompanyId], source.[Name], source.[CountryId], source.[BusinessTypeId], source.[CompanyTypeId], source.[Address], source.[Active], source.[PhoneNumber], source.[EmailAddress], source.[City], source.[LegalName], source.[PostalCode], source.[ParentCompanyId]
    FROM [Wh_Staging_Procurement].[company].[Company] AS source
    LEFT JOIN [company].[Company] AS target
    ON source.[CompanyId] = target.[CompanyId]
    WHERE target.[CompanyId] IS NULL;

END;
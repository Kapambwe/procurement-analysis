-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
CREATE PROCEDURE [tender].[UpdateOrInsertIntoDocumentType]
AS
BEGIN
    -- SET NOCOUNT ON added to prevent extra result sets from
    -- interfering with SELECT statements.
    SET NOCOUNT ON;

    -- Update existing records
    UPDATE target
    SET
        target.[Name] = source.[Name],
        target.[Code] = source.[Code],
        target.[Description] = source.[Description]
    FROM [tender].[DocumentType] AS target
    INNER JOIN [Wh_Staging_Procurement].[tender].[DocumentType] AS source
    ON target.[DocumentTypeId] = source.[DocumentTypeId];

    -- Insert new records
    INSERT INTO [tender].[DocumentType] ([DocumentTypeId], [Name], [Code], [Description])
    SELECT source.[DocumentTypeId], source.[Name], source.[Code], source.[Description]
    FROM [Wh_Staging_Procurement].[tender].[DocumentType] AS source
    LEFT JOIN [tender].[DocumentType] AS target
    ON source.[DocumentTypeId] = target.[DocumentTypeId]
    WHERE target.[DocumentTypeId] IS NULL;

END;
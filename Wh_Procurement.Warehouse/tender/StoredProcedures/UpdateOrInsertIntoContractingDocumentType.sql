-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
CREATE PROCEDURE [tender].[UpdateOrInsertIntoContractingDocumentType]
AS
BEGIN
    -- SET NOCOUNT ON added to prevent extra result sets from
    -- interfering with SELECT statements.
    SET NOCOUNT ON;

    -- Update existing records
    UPDATE target
    SET
        target.[Section] = source.[Section],
        target.[Category] = source.[Category],
        target.[DocumentTypeId] = source.[DocumentTypeId]
    FROM [tender].[ContractingDocumentType] AS target
    INNER JOIN [Wh_Staging_Procurement].[tender].[ContractingDocumentType] AS source
    ON target.[ContractingDocumentTypeId] = source.[ContractingDocumentTypeId];

    -- Insert new records
    INSERT INTO [tender].[ContractingDocumentType] ([ContractingDocumentTypeId], [Section], [Category], [DocumentTypeId])
    SELECT source.[ContractingDocumentTypeId], source.[Section], source.[Category], source.[DocumentTypeId]
    FROM [Wh_Staging_Procurement].[tender].[ContractingDocumentType] AS source
    LEFT JOIN [tender].[ContractingDocumentType] AS target
    ON source.[ContractingDocumentTypeId] = target.[ContractingDocumentTypeId]
    WHERE target.[ContractingDocumentTypeId] IS NULL;

END;
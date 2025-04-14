-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
CREATE PROCEDURE [tender].[UpdateOrInsertIntoContractingStage]
AS
BEGIN
    -- SET NOCOUNT ON added to prevent extra result sets from
    -- interfering with SELECT statements.
    SET NOCOUNT ON;

    -- Update existing records
    UPDATE target
    SET
        target.[Name] = source.[Name]
    FROM [tender].[ContractingStage] AS target
    INNER JOIN [Wh_Staging_Procurement].[list].[ContractingStage] AS source
    ON target.[ContractingStageId] = source.[ContractingStageId];

    -- Insert new records
    INSERT INTO [tender].[ContractingStage] ([ContractingStageId], [Name])
    SELECT source.[ContractingStageId], source.[Name]
    FROM [Wh_Staging_Procurement].[list].[ContractingStage] AS source
    LEFT JOIN [tender].[ContractingStage] AS target
    ON source.[ContractingStageId] = target.[ContractingStageId]
    WHERE target.[ContractingStageId] IS NULL;

END;
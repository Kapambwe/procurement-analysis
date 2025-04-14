-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
CREATE PROCEDURE [tender].[UpdateOrInsertIntoProduct]
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
        target.[Classification] = source.[Classification],
        target.[Scheme] = source.[Scheme],
        target.[ExternalId] = source.[ExternalId],
        target.[Uri] = source.[Uri]
    FROM [tender].[Product] AS target
    INNER JOIN [Wh_Staging_Procurement].[tender].[Product] AS source
    ON target.[ProductId] = source.[ProductId];

    -- Insert new records
    INSERT INTO [tender].[Product] ([ProductId], [Name], [Description], [Classification], [Scheme], [ExternalId], [Uri])
    SELECT 
        source.[ProductId], 
        source.[Name], 
        source.[Description], 
        source.[Classification], 
        source.[Scheme], 
        source.[ExternalId], 
        source.[Uri]
    FROM [Wh_Staging_Procurement].[tender].[Product] AS source
    LEFT JOIN [tender].[Product] AS target
    ON source.[ProductId] = target.[ProductId]
    WHERE target.[ProductId] IS NULL;

END;
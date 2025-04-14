-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
CREATE PROCEDURE [tender].[UpdateOrInsertIntoDatePeriod]
AS
BEGIN
    -- SET NOCOUNT ON added to prevent extra result sets from
    -- interfering with SELECT statements.
    SET NOCOUNT ON;

    -- Update existing records
    UPDATE target
    SET
        target.[StartDate] = source.[StartDate],
        target.[EndDate] = source.[EndDate]
    FROM [tender].[TenderPeriod] AS target
    INNER JOIN [Wh_Staging_Procurement].[tender].[TenderPeriod] AS source
    ON target.[TenderPeriodId] = source.[TenderPeriodId];

    -- Insert new records
    INSERT INTO [tender].[TenderPeriod] ([TenderPeriodId], [StartDate], [EndDate])
    SELECT source.[TenderPeriodId], source.[StartDate], source.[EndDate]
    FROM [Wh_Staging_Procurement].[tender].[TenderPeriod] AS source
    LEFT JOIN [tender].[TenderPeriod] AS target
    ON source.[TenderPeriodId] = target.[TenderPeriodId]
    WHERE target.[TenderPeriodId] IS NULL;

END;
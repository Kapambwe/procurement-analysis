CREATE PROCEDURE tender.usp_FlagInvitationOnlyTenders
AS
BEGIN
    SET NOCOUNT ON;

    DECLARE @RedFlagId INT;
    DECLARE @MaxTenderRedFlagId INT;

    -- Fetch the RedFlagId for 'Tender is invitation only'
    SELECT TOP 1 @RedFlagId = RedFlagId
    FROM [tender].[RedFlags]
    WHERE Red_Flag = 'Tender is invitation only';

    -- Fetch the current maximum TenderRedFlagId
    SELECT @MaxTenderRedFlagId = ISNULL(MAX(TenderRedFlagId), 0)
    FROM [Wh_Procurement].[tender].[TenderRedFlag];

    -- Step 1: Identify tenders using invitation-only procurement methods
    WITH InvitationOnlyTenders AS (
        SELECT 
            t.TenderId,
            t.Amount,
            t.Description,
            t.ProcurementMethodId,
            pm.Name AS ProcurementMethodName,
            pm.Description AS ProcurementMethodDescription,
            t.ProcurementMethodRationaleId,
            pmr.Name AS ProcurementMethodRationaleName,
            pmr.Description AS ProcurementMethodRationaleDescription
        FROM 
            [Wh_Procurement].[tender].[Tender] t
        JOIN 
            [Wh_Procurement].[tender].[ProcurementMethod] pm ON t.ProcurementMethodId = pm.ProcurementMethodId
        JOIN 
            [Wh_Procurement].[tender].[ProcurementMethodRationale] pmr ON t.ProcurementMethodRationaleId = pmr.ProcurementMethodRationaleId
        WHERE 
            pm.Name IN ('limited', 'selective')
    )

    -- Step 2: Insert into TenderRedFlag
    INSERT INTO [Wh_Procurement].[tender].[TenderRedFlag] (
        TenderRedFlagId,
        RedFlagId,
        TenderId,
        TrackDateTime,
        Value,
        ValueType
    )
    SELECT 
        ROW_NUMBER() OVER (ORDER BY TenderId) + @MaxTenderRedFlagId AS TenderRedFlagId,
        @RedFlagId AS RedFlagId,
        TenderId,
        GETDATE() AS TrackDateTime,
        ProcurementMethodName AS Value, -- Assuming Amount is the relevant column
        'string' AS ValueType
    FROM 
        InvitationOnlyTenders;
END;
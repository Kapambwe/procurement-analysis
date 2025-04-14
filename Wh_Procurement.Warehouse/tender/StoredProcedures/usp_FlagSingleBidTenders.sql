CREATE PROCEDURE tender.usp_FlagSingleBidTenders
AS
BEGIN
    SET NOCOUNT ON;

    DECLARE @RedFlagId INT;
    DECLARE @MaxTenderRedFlagId INT;

    -- Fetch the RedFlagId for 'Single bid received'
        SELECT TOP 1 @RedFlagId = RedFlagId
    FROM [tender].[RedFlag]
    WHERE Red_Flag = 'Single bid received';

    -- Fetch the current maximum TenderRedFlagId
    SELECT @MaxTenderRedFlagId = ISNULL(MAX(TenderRedFlagId), 0)
    FROM [Wh_Procurement].[tender].[TenderRedFlag];

    -- Step 1: Identify competitive procedures and single bid tenders
    WITH CompetitiveSingleBidTenders AS (
        SELECT 
            TenderId,
            NumberofTenderers
        FROM 
            [Wh_Procurement].[tender].[Tender]
        WHERE 
            NumberofTenderers = 1
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
        NumberofTenderers AS Value,
        'int' AS ValueType
    FROM 
        CompetitiveSingleBidTenders;
END;
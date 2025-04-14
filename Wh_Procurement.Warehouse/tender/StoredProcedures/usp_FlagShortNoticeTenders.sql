CREATE PROCEDURE tender.usp_FlagShortNoticeTenders
AS
BEGIN
    SET NOCOUNT ON;

    DECLARE @RedFlagId INT;
    DECLARE @MaxTenderRedFlagId INT;
    DECLARE @Threshold INT = 3; -- Define the threshold for the number of days

    -- Fetch the RedFlagId for 'Short or inadequate notice to bidders'
    SELECT TOP 1 @RedFlagId = RedFlagId
    FROM [tender].[RedFlag]
    WHERE Red_Flag = 'Short or inadequate notice to bidders to submit expressions of interest or bids';

    -- Fetch the current maximum TenderRedFlagId
    SELECT @MaxTenderRedFlagId = ISNULL(MAX(TenderRedFlagId), 0)
    FROM [Wh_Procurement].[tender].[TenderRedFlag];

    -- Step 1: Calculate the number of days for the bidding period
    WITH TenderBiddingPeriod AS (
        SELECT 
            t.TenderId,
            DATEDIFF(DAY, tp.StartDate, tp.EndDate) AS BiddingPeriodDays
        FROM 
            [Wh_Procurement].[tender].[Tender] t
        JOIN 
            [Wh_Procurement].[tender].[TenderPeriod] tp ON t.TenderPeriodId = tp.TenderPeriodId
    )

    -- Step 2: Identify tenders with short or inadequate notice periods
    , ShortNoticeTenders AS (
        SELECT 
            TenderId,
            BiddingPeriodDays
        FROM 
            TenderBiddingPeriod
        WHERE 
            BiddingPeriodDays < @Threshold
    )

    -- Step 3: Insert into TenderRedFlag
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
        BiddingPeriodDays AS Value,
        'int' AS ValueType
    FROM 
        ShortNoticeTenders;
END;
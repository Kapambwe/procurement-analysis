CREATE PROCEDURE [tender].[usp_CalculateCorruptionIndexScores]
AS
BEGIN

    -- Get the maximum CorruptionRiskScoreId
    DECLARE @MaxCorruptionRiskScoreId INT;
    SELECT @MaxCorruptionRiskScoreId = ISNULL(MAX(CorruptionRiskScoreId), 0) FROM [tender].[CorruptionRiskScore];

    -- Insert new records into the CorruptionRiskScore table if TenderRedFlagId does not exist
    INSERT INTO [tender].[CorruptionRiskScore] (CorruptionRiskScoreId, TenderRedFlagId, TrackDateTime, Value)
    SELECT 
        ROW_NUMBER() OVER (ORDER BY trf.[TenderRedFlagId]) + @MaxCorruptionRiskScoreId AS CorruptionRiskScoreId,
        trf.[TenderRedFlagId],
        trf.[TrackDateTime],
        1 AS CorruptionIndexScore
    FROM 
        [tender].[TenderRedFlag] trf
    JOIN [tender].[RedFlag] rf
    ON trf.[RedFlagId] = rf.[RedFlagId]
    LEFT JOIN [tender].[CorruptionRiskScore] crs
    ON trf.[TenderRedFlagId] = crs.[TenderRedFlagId]
    WHERE trf.[RedFlagId] IN (20, 15, 3)
    AND crs.[TenderRedFlagId] IS NULL;
END;
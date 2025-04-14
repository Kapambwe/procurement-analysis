CREATE PROCEDURE [tender].[usp_InsertTenderCorruptionIndex]
AS
BEGIN
    SET NOCOUNT ON;

    -- Calculate the sum of corruption risk scores for each TenderId, divide by four, and ensure unique results for TenderId with TenderStatusId of 3 or 1
    WITH CorruptionScores AS (
        SELECT 
            trf.TenderId,
            SUM(crs.Value) AS TotalCorruptionScore
        FROM 
            [tender].[TenderRedFlag] trf
        JOIN 
            [tender].[CorruptionRiskScore] crs ON trf.TenderRedFlagId = crs.TenderRedFlagId
        JOIN 
            [tender].[Tender] t ON trf.TenderId = t.TenderId
        WHERE 
            t.TenderStatusId IN (3, 1)
        GROUP BY 
            trf.TenderId
    )
    INSERT INTO [tender].[TenderCorruptionIndex] (TenderId, CorruptionIndexScore, TrackDateTime)
    SELECT 
        cs.TenderId,
        CAST(cs.TotalCorruptionScore / 4.0 AS DECIMAL(10, 3)) AS CorruptionIndexScore,
        GETDATE() AS TrackDateTime
    FROM 
        CorruptionScores cs
    WHERE 
        NOT EXISTS (
            SELECT 1
            FROM [tender].[TenderCorruptionIndex] tci
            WHERE tci.TenderId = cs.TenderId
        );
END;
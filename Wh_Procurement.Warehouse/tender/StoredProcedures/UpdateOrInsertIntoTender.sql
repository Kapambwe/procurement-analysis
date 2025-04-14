-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
CREATE PROCEDURE [tender].[UpdateOrInsertIntoTender]
AS
BEGIN
    -- SET NOCOUNT ON added to prevent extra result sets from
    -- interfering with SELECT statements.
    SET NOCOUNT ON;

    -- Update existing records
    UPDATE target
    SET
        target.[Amount] = source.[Amount],
        target.[Description] = source.[Description],
        target.[Name] = source.[Title],
        target.[EquiryPeriodId] = source.[TenderPeriodId],
        target.[HasEquiry] = source.[HasEquiry],
        target.[SubmittionMethodDetail] = source.[SubmittionMethodDetail],
        target.[NumberofTenderers] = source.[NumberofTenderers],
        target.[TenderPeriodId] = source.[TenderPeriodId],
        target.[CurrencyId] = source.[CurrencyId],
        target.[ExternalId] = source.[ExternalId],
        target.[AwardCriteriaId] = source.[AwardCriteriaId],
        target.[AwardCriteriaDetailId] = source.[AwardCriteriaDetailId],
        target.[EligibilityCriteriaId] = source.[EligibilityCriteriaId],
        target.[ProcurementMethodId] = source.[ProcurementMethodId],
        target.[ProcurementMethodRationaleId] = source.[ProcurementMethodRationaleId],
        target.[SubmissionMethodId] = source.[SubmissionMethodId],
        target.[SubmittionMethodDetailId] = source.[SubmissionMethodDetailId],
        target.[TenderStatusId] = source.[TenderStatusId],
        target.[ProcuringCompanyId] = source.[ProcuringCompanyId]
    FROM [tender].[Tender] AS target
    INNER JOIN (
        SELECT 
            t.TenderId,
            t.Amount,
            t.Description,
            t.Title,
            t.[HasEquiry],
            t.[SubmittionMethodDetail],
            t.[NumberofTenderers],
            t.[TenderPeriodId],
            t.[CurrencyId],
            t.[ExternalId],
            ac.AwardCriteriaId AS AwardCriteriaId,
            acd.[AwardCriteriaDetailId],
            ec.[EligibilityCriteriaId],
            pm.[ProcurementMethodId],
            pmr.[ProcurementMethodRationaleId],
            sm.[SubmissionMethodId] AS SubmissionMethodId,
            smd.[SubmissionMethodDetailId] AS SubmissionMethodDetailId,
            ts.[TenderStatusId],
            c.CompanyId AS ProcuringCompanyId,
            p.ProductId,
            ti.Quantity,
            p.Classification,
            c.Name as Company 
        FROM [Wh_Staging_Procurement].tender.Tender t 
        JOIN [Wh_Staging_Procurement].tender.AwardCriteria ac ON t.AwardCriteria = ac.Name 
        JOIN [Wh_Staging_Procurement].tender.ContractingProcess cp ON t.TenderId = cp.TenderId
        JOIN [Wh_Staging_Procurement].company.Company c ON c.CompanyId = cp.CompanyId
        JOIN [Wh_Staging_Procurement].tender.SubmissionMethod sm ON t.SubmittionMethod = sm.Name 
        LEFT JOIN [Wh_Staging_Procurement].tender.SubmissionMethodDetail smd ON t.SubmittionMethodDetail = smd.Name 
        JOIN [Wh_Staging_Procurement].tender.AwardCriteriaDetail acd ON t.AwardCriteriaDetail = acd.Name 
        JOIN [Wh_Staging_Procurement].tender.EligibilityCriteria ec ON t.EligibilityCriteria = ec.Name 
        JOIN [Wh_Staging_Procurement].tender.ProcurementMethod pm ON t.ProcurementMethod = pm.Name 
        JOIN [Wh_Staging_Procurement].tender.ProcurementMethodRationale pmr ON t.ProcurementMethodRationale = pmr.Name 
        JOIN [Wh_Staging_Procurement].tender.TenderStatus ts ON t.Status = ts.Name 
        LEFT JOIN [Wh_Staging_Procurement].tender.TenderItem ti ON ti.ContractingProcessId = cp.ContractingProcessId
        LEFT JOIN [Wh_Staging_Procurement].tender.Product p ON p.ProductId = ti.ProductId
    ) AS source
    ON target.[TenderId] = source.[TenderId];

    -- Insert new records
    INSERT INTO [tender].[Tender] ([TenderId], [Amount], [Description], [Name], [EquiryPeriodId], [HasEquiry], [SubmittionMethodDetail], [NumberofTenderers], [TenderPeriodId], [CurrencyId], [ExternalId], [AwardCriteriaId], [AwardCriteriaDetailId], [EligibilityCriteriaId], [ProcurementMethodId], [ProcurementMethodRationaleId], [SubmissionMethodId], [SubmittionMethodDetailId], [TenderStatusId], [ProcuringCompanyId])
    SELECT 
        source.[TenderId], 
        source.[Amount], 
        source.[Description], 
        source.[Title], 
        source.[TenderPeriodId], 
        source.[HasEquiry], 
        source.[SubmittionMethodDetail], 
        source.[NumberofTenderers], 
        source.[TenderPeriodId], 
        source.[CurrencyId], 
        source.[ExternalId], 
        source.[AwardCriteriaId], 
        source.[AwardCriteriaDetailId], 
        source.[EligibilityCriteriaId], 
        source.[ProcurementMethodId], 
        source.[ProcurementMethodRationaleId], 
        source.[SubmissionMethodId], 
        source.[SubmissionMethodDetailId], 
        source.[TenderStatusId], 
        source.[ProcuringCompanyId]
    FROM (
        SELECT 
            t.TenderId,
            t.Amount,
            t.Description,
            t.Title,
            t.[HasEquiry],
            t.[SubmittionMethodDetail],
            t.[NumberofTenderers],
            t.[TenderPeriodId],
            t.[CurrencyId],
            t.[ExternalId],
            ac.AwardCriteriaId AS AwardCriteriaId,
            acd.[AwardCriteriaDetailId],
            ec.[EligibilityCriteriaId],
            pm.[ProcurementMethodId],
            pmr.[ProcurementMethodRationaleId],
            sm.[SubmissionMethodId] AS SubmissionMethodId,
            smd.[SubmissionMethodDetailId] AS SubmissionMethodDetailId,
            ts.[TenderStatusId],
            c.CompanyId AS ProcuringCompanyId,
            p.ProductId,
            ti.Quantity,
            p.Classification,
            c.Name as Company 
        FROM [Wh_Staging_Procurement].tender.Tender t 
        JOIN [Wh_Staging_Procurement].tender.AwardCriteria ac ON t.AwardCriteria = ac.Name 
        JOIN [Wh_Staging_Procurement].tender.ContractingProcess cp ON t.TenderId = cp.TenderId
        JOIN [Wh_Staging_Procurement].company.Company c ON c.CompanyId = cp.CompanyId
        JOIN [Wh_Staging_Procurement].tender.SubmissionMethod sm ON t.SubmittionMethod = sm.Name 
        LEFT JOIN [Wh_Staging_Procurement].tender.SubmissionMethodDetail smd ON t.SubmittionMethodDetail = smd.Name 
        JOIN [Wh_Staging_Procurement].tender.AwardCriteriaDetail acd ON t.AwardCriteriaDetail = acd.Name 
        JOIN [Wh_Staging_Procurement].tender.EligibilityCriteria ec ON t.EligibilityCriteria = ec.Name 
        JOIN [Wh_Staging_Procurement].tender.ProcurementMethod pm ON t.ProcurementMethod = pm.Name 
        JOIN [Wh_Staging_Procurement].tender.ProcurementMethodRationale pmr ON t.ProcurementMethodRationale = pmr.Name 
        JOIN [Wh_Staging_Procurement].tender.TenderStatus ts ON t.Status = ts.Name 
        LEFT JOIN [Wh_Staging_Procurement].tender.TenderItem ti ON ti.ContractingProcessId = cp.ContractingProcessId
        LEFT JOIN [Wh_Staging_Procurement].tender.Product p ON p.ProductId = ti.ProductId
    ) AS source
    LEFT JOIN [tender].[Tender] AS target
    ON source.[TenderId] = target.[TenderId]
    WHERE target.[TenderId] IS NULL;

END;
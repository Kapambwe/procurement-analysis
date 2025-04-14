CREATE TABLE [tender].[Tender] (

	[TenderId] int NOT NULL, 
	[Amount] decimal(20,4) NULL, 
	[Description] varchar(8000) NULL, 
	[Name] varchar(8000) NULL, 
	[EquiryPeriodId] int NULL, 
	[HasEquiry] bit NULL, 
	[SubmittionMethodDetail] varchar(8000) NULL, 
	[NumberofTenderers] int NULL, 
	[TenderPeriodId] int NULL, 
	[CurrencyId] int NULL, 
	[ExternalId] varchar(1000) NULL, 
	[AwardCriteriaId] int NULL, 
	[AwardCriteriaDetailId] int NULL, 
	[EligibilityCriteriaId] int NULL, 
	[ProcurementMethodId] int NULL, 
	[ProcurementMethodRationaleId] int NULL, 
	[SubmissionMethodId] int NULL, 
	[SubmittionMethodDetailId] int NULL, 
	[TenderStatusId] int NULL, 
	[ProcuringCompanyId] int NULL, 
	[FundingCompanyId] int NULL, 
	[ProductId] int NULL, 
	[Quantity] decimal(18,0) NULL, 
	[UnitId] int NULL, 
	[AwardStartDate] datetime2(6) NULL, 
	[AwardEndDate] datetime2(6) NULL, 
	[EnquiryStartDate] datetime2(6) NULL, 
	[EnquiryEndDate] datetime2(6) NULL, 
	[InitiationType] varchar(400) NULL
);


GO
ALTER TABLE [tender].[Tender] ADD CONSTRAINT PK_Tender primary key NONCLUSTERED ([TenderId]);
GO
ALTER TABLE [tender].[Tender] ADD CONSTRAINT FK_Tender_AwardCriteria FOREIGN KEY ([AwardCriteriaId]) REFERENCES [tender].[AwardCriteria]([AwardCriteriaId]);
GO
ALTER TABLE [tender].[Tender] ADD CONSTRAINT FK_Tender_AwardCriteriaDetail FOREIGN KEY ([AwardCriteriaDetailId]) REFERENCES [tender].[AwardCriteriaDetail]([AwardCriteriaDetailId]);
GO
ALTER TABLE [tender].[Tender] ADD CONSTRAINT FK_Tender_EligibilityCriteria FOREIGN KEY ([EligibilityCriteriaId]) REFERENCES [tender].[EligibilityCriteria]([EligibilityCriteriaId]);
GO
ALTER TABLE [tender].[Tender] ADD CONSTRAINT FK_Tender_FundingCompany FOREIGN KEY ([FundingCompanyId]) REFERENCES [company].[Company]([CompanyId]);
GO
ALTER TABLE [tender].[Tender] ADD CONSTRAINT FK_Tender_ProcurementMethod FOREIGN KEY ([ProcurementMethodId]) REFERENCES [tender].[ProcurementMethod]([ProcurementMethodId]);
GO
ALTER TABLE [tender].[Tender] ADD CONSTRAINT FK_Tender_ProcurementMethodRationale FOREIGN KEY ([ProcurementMethodRationaleId]) REFERENCES [tender].[ProcurementMethodRationale]([ProcurementMethodRationaleId]);
GO
ALTER TABLE [tender].[Tender] ADD CONSTRAINT FK_Tender_ProcuringCompany FOREIGN KEY ([ProcuringCompanyId]) REFERENCES [company].[Company]([CompanyId]);
GO
ALTER TABLE [tender].[Tender] ADD CONSTRAINT FK_Tender_Product FOREIGN KEY ([ProductId]) REFERENCES [tender].[Product]([ProductId]);
GO
ALTER TABLE [tender].[Tender] ADD CONSTRAINT FK_Tender_SubmissionMethod FOREIGN KEY ([SubmissionMethodId]) REFERENCES [tender].[SubmissionMethod]([SubmissionMethodId]);
GO
ALTER TABLE [tender].[Tender] ADD CONSTRAINT FK_Tender_SubmittionMethodDetail FOREIGN KEY ([SubmittionMethodDetailId]) REFERENCES [tender].[SubmissionMethodDetail]([SubmissionMethodDetailId]);
GO
ALTER TABLE [tender].[Tender] ADD CONSTRAINT FK_Tender_TenderPeriodId FOREIGN KEY ([TenderPeriodId]) REFERENCES [tender].[TenderPeriod]([TenderPeriodId]);
GO
ALTER TABLE [tender].[Tender] ADD CONSTRAINT FK_Tender_TenderStatus FOREIGN KEY ([TenderStatusId]) REFERENCES [tender].[TenderStatus]([TenderStatusId]);
GO
ALTER TABLE [tender].[Tender] ADD CONSTRAINT FK_Tender_Unit FOREIGN KEY ([UnitId]) REFERENCES [tender].[Units]([UnitsId]);
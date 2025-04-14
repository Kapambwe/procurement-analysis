CREATE TABLE [tender].[Tender] (

	[TenderId] int NOT NULL, 
	[Amount] decimal(20,4) NULL, 
	[ProcurementMethodRationale] varchar(8000) NULL, 
	[Description] varchar(8000) NULL, 
	[Title] varchar(8000) NULL, 
	[SubmittionMethod] varchar(8000) NULL, 
	[ProcurementMethod] varchar(8000) NULL, 
	[EquiryPeriodStartDate] datetime2(6) NULL, 
	[EquiryPeriodEndDate] datetime2(6) NULL, 
	[AwardCriteria] varchar(8000) NULL, 
	[EligibilityCriteria] varchar(8000) NULL, 
	[AwardCriteriaDetail] varchar(8000) NULL, 
	[HasEquiry] bit NULL, 
	[SubmittionMethodDetail] varchar(8000) NULL, 
	[NumberofTenderers] int NULL, 
	[CompanyId] int NULL, 
	[AssetId] int NULL, 
	[Status] varchar(8000) NULL, 
	[ReleaseId] varchar(8000) NULL, 
	[OcdsId] varchar(8000) NULL, 
	[ReleaseDate] datetime2(6) NULL, 
	[ReleaseTag] varchar(8000) NULL, 
	[TenderPeriodId] int NULL, 
	[CurrencyId] int NULL, 
	[ExternalId] varchar(8000) NULL, 
	[AwardCriteriaId] int NULL, 
	[AwardCriteriaDetailId] int NULL, 
	[EligibilityCriteriaId] int NULL, 
	[ProcurementMethodId] int NULL, 
	[ProcurementMethodRationaleId] int NULL, 
	[SubmissionMethodId] int NULL, 
	[SubmittionMethodDetailId] int NULL, 
	[TenderStatusId] int NULL
);


GO
ALTER TABLE [tender].[Tender] ADD CONSTRAINT PK_Tender primary key NONCLUSTERED ([TenderId]);
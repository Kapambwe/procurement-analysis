CREATE TABLE [company].[Company] (

	[CompanyId] int NOT NULL, 
	[Name] varchar(8000) NOT NULL, 
	[Description] varchar(8000) NULL, 
	[Exchange] varchar(8000) NULL, 
	[ExchangeSymbol] varchar(50) NULL, 
	[CEO] varchar(100) NULL, 
	[MarketCap] decimal(18,2) NULL, 
	[Employee] bigint NULL, 
	[Logo] varchar(8000) NULL, 
	[BloomBerg] varchar(8000) NULL, 
	[Active] bit NULL, 
	[IsReviewble] bit NULL, 
	[CIK] varchar(50) NULL, 
	[Address] varchar(100) NULL, 
	[PhoneNumber] varchar(50) NULL, 
	[Location] varchar(100) NULL, 
	[ContinentId] int NOT NULL, 
	[ParentCompanyId] int NULL, 
	[RegionAreaId] int NULL, 
	[CountryId] int NOT NULL, 
	[BusinessTypeId] int NULL, 
	[CompanyTypeId] int NULL, 
	[TrackDateTime] datetime2(6) NULL, 
	[UpdatedDateTime] datetime2(6) NULL, 
	[NationRank] int NULL, 
	[BankId] int NULL, 
	[IssueType] varchar(50) NULL, 
	[PrimarySicCode] int NULL, 
	[Beta] decimal(8,4) NULL, 
	[Currency] varchar(50) NULL, 
	[FIGI] varchar(50) NULL, 
	[IndustryId] int NULL, 
	[WebAddress] varchar(500) NULL, 
	[EmailAddress] varchar(500) NULL, 
	[City] varchar(500) NULL, 
	[LegalName] varchar(8000) NULL, 
	[PostalCode] varchar(100) NULL, 
	[Region] varchar(100) NULL
);


GO
ALTER TABLE [company].[Company] ADD CONSTRAINT PK_Company primary key NONCLUSTERED ([CompanyId]);
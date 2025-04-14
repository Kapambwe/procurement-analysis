-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
CREATE PROCEDURE [meta].[Get_WhProcurement_Metadata]
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;
SELECT [TargetSchema]
      ,[TargetTable]
      ,[SourceSchema]
      ,[SourceTable]
      ,[StagingSchema]
      ,[StagingTable]
      ,[StagingDatabase]
      ,[LoadType]
      ,[LoadIndicator]
      ,[ETLStrategy]
      ,[SourceStoredProcedureName]
      ,[TargetStoredProcedureName]
      ,[ColumnKey]
      ,[NumberOfPrimaryKeyColumns]
      ,[WaterfallColumn]
      ,[TableColumns]
      ,[ExecutionOrder]
  FROM [meta].[WhProcurement_Metadata]
  WHERE  TargetStoredProcedureName IS NOT NULL
  ORDER BY ExecutionOrder
END
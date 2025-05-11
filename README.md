# Open Contracting Data Analysis for Corruption Risk Detection

This project analyzes open contracting data to identify potential corruption risks in public procurement processes.

## Project Overview

- **Data Processing**: Ingested, cleaned, and transformed open contracting data (JSON) into a Lakehouse and Warehouse environment.
- **Risk Scoring**: Calculated corruption risk scores for factors like single-bid contracts, repeated awards, short tendering periods, and unusual price variations.
- **Power BI Reporting**: Created interactive dashboards for visualizing corruption risk indicators.
- **Technologies Used**: Microsoft Fabric, Power BI, JSON, Data Lakehouse/Warehousing.

## Key Visualizations

Here are the key visualizations from our analysis:

![Percentange Between Values](percentangebetweenvalues.jpg)

![Average Bid by Procurement Method](AverageBidByProcurement.jpg)

*Average bid amounts across different procurement methods*

![Average Bidders by Contract Value](AverageBiddersByContractValue.jpg)

*Relationship between contract value and number of bidders*

![Average Number of Bids](AverageNumberOfBids.jpg)
*Distribution of bids received per contract*

![Contracts by Procuring Entity](ContractByProcuringEntity.jpg)

*Volume of contracts awarded by different procuring entities*

![Contracts by Procurement Method](ContractsByProcurement.jpg)

*Breakdown of contracts by procurement type*

![Contracts by Procurement Method](ContractsByProcurementMethod.jpg)

*Detailed view of procurement methods used*

![Contracts by Selected Procuring Entity](ContractsByProcuringSelectedEntity.jpg)

*Contract distribution for specific entities of interest*

![Efficiency and Potential Loss](EfficiencyAndPotentialLoss.jpg)

*Analysis of procurement efficiency and potential financial losses*

![image](https://github.com/user-attachments/assets/9cac8fdf-0ea0-4a70-9830-0dd19f6d98a6)

*Analysis of Average Score by Procurement Entity and Year*

![Limited Procurement Methods](LimitedNumberOfProcurementMethods.jpg)

*Prevalence of limited/non-competitive procurement methods*

![Open Tendering Percentage](OpenTenderingPercentage.jpg)

*Percentage of contracts awarded through open tendering*

## Getting Started

To replicate this analysis:
1. Set up a Microsoft Fabric environment
2. Ingest JSON contracting data into a Lakehouse
3. Transform the data using the provided scripts
4. Connect Power BI to the processed data
5. Use the dashboard templates to visualize the results

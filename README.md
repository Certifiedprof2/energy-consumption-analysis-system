# Energy Consumption Analysis System 

## Problem Statement

Electricity access and reliable electricity supply remain important challenges in many parts of Sub-Saharan Africa. However, having access to electricity does not necessarily mean that electricity consumption is being properly monitored, analyzed, or understood.

Without structured analysis of electricity consumption records, it can be difficult to identify high-consuming customers, understand consumption patterns across different locations and customer types, monitor electricity costs, and identify customers that may require further attention.

This project investigates electricity consumption data by developing a Python-based Energy Consumption Analysis System that organizes, validates, and analyzes structured electricity records to produce useful information for decision-making.

---

## Project Objective

The objective of this project is to develop a Python-based Energy Consumption Analysis System that can organize and validate electricity consumption records and generate useful analytical insights.

The system is designed to:

- Calculate total and average electricity consumption.
- Identify the highest and lowest consumers.
- Calculate individual and total electricity costs.
- Analyze consumption by location.
- Analyze consumption by customer type.
- Analyze monthly consumption.
- Classify customers into Low, Medium, and High consumption categories.
- Identify high-attention customers based on consumption and renewable energy share.
- Provide an interactive menu-driven system for accessing the analysis.

---

## Industry Context

Energy consumption analysis is important for understanding how electricity is being used across different customers, locations, and sectors.

For energy providers and other stakeholders, consumption analysis can support:

- Energy demand planning.
- Identification of high-consumption customers.
- Energy-efficiency initiatives.
- Renewable energy planning.
- Infrastructure and electricity-access planning.
- Cost and affordability analysis.
- Evidence-based decision-making.

By transforming electricity records into structured information, data analysis can help stakeholders understand consumption patterns and identify areas that may require further investigation.

---

## Dataset

### Source

The dataset was created as a **simulated instructional dataset** for the Python Study Group project.

The data is not official Nigerian utility or NERC data.

### Number of Records

The dataset contains **20 customer records**.

### Variables

The dataset contains the following variables:

- Customer ID
- Customer Name
- Customer Type
- Location
- Month
- Consumption (kWh)
- Tariff
- Peak Consumption (kWh)
- Renewable Share (%)
- Outage Hours
- Payment Status

### Time Period

The records cover **January to June**.

### Geography

The dataset covers three locations:

- Lagos
- Abuja
- Ibadan

### Customer Types

The dataset includes:

- Residential
- SME
- Industrial
- Hospital
- School
- Agricultural

### Data Type

The dataset is **simulated and instructional** and was created to demonstrate the use of Python for organizing, validating, and analyzing electricity consumption data.

---

## Methodology

The analysis was implemented using Python.

The dataset was structured using lists and dictionaries, while functions were created to perform calculations and different types of analysis.

### Analysis Process

1. Created and organized the 20 electricity consumption records.
2. Validated the records to identify invalid or inconsistent values.
3. Calculated total electricity consumption.
4. Calculated average electricity consumption.
5. Identified the highest and lowest consumers.
6. Calculated individual electricity costs.
7. Calculated total and average electricity costs.
8. Grouped electricity consumption by location.
9. Grouped electricity consumption by customer type.
10. Calculated monthly consumption totals.
11. Classified customers into Low, Medium, and High consumption categories.
12. Identified high-attention customers based on consumption and renewable energy share.
13. Implemented an interactive menu-driven system using loops and functions.

### Consumption Classification

Customers were classified using the following thresholds:

| Classification | Consumption |
|---|---:|
| Low | < 500 kWh |
| Medium | 500–999 kWh |
| High | ≥ 1,000 kWh |

### High-Attention Rule

A customer was identified as a high-attention customer when both conditions were met:

- Consumption was **≥ 1,000 kWh**
- Renewable share was **< 15%**

This rule was created for the project to identify customers with relatively high electricity consumption and relatively low renewable energy share.

---

## Key Findings

The analysis produced the following findings:

### 1. Total Electricity Consumption

The 20 records produced a total electricity consumption of:

**24,240 kWh**

The average consumption was:

**1,212 kWh per record**

### 2. Total Electricity Cost

The calculated total electricity cost was:

**₦2,920,000**

The average electricity cost was:

**₦146,000 per record**

Electricity cost was calculated using:

**Electricity Cost = Consumption × Tariff**

### 3. Highest and Lowest Consumers

The highest individual consumer was:

**Industrial Works Ltd — 3,600 kWh**

The lowest individual consumer was:

**Hope Residence — 190 kWh**

### 4. Location Analysis

Total consumption by location was:

| Location | Consumption |
|---|---:|
| Lagos | 9,760 kWh |
| Abuja | 8,090 kWh |
| Ibadan | 6,390 kWh |

Lagos recorded the highest total consumption among the three locations.

### 5. Customer Type Analysis

Consumption by customer type was:

| Customer Type | Consumption |
|---|---:|
| Industrial | 9,600 kWh |
| Hospital | 4,150 kWh |
| SME | 4,050 kWh |
| Agricultural | 3,580 kWh |
| School | 1,640 kWh |
| Residential | 1,220 kWh |

Industrial customers accounted for approximately **40% of total recorded consumption**, despite having only three records in the dataset.

### 6. Monthly Consumption

Monthly consumption totals were:

| Month | Consumption |
|---|---:|
| January | 2,580 kWh |
| February | 1,940 kWh |
| March | 6,050 kWh |
| April | 2,200 kWh |
| May | 3,750 kWh |
| June | 7,720 kWh |

June recorded the highest monthly total, while February recorded the lowest.

However, these figures should not be interpreted as a reliable seasonal trend because each customer appears only once in the dataset.

### 7. Consumption Classification

**9 of the 20 records** were classified as High consumption using the project's threshold of ≥1,000 kWh.

### 8. High-Attention Customers

Four customers met the project's high-attention criteria:

- Prime Plastics
- Lakeside Hotel
- Naija Foods Ltd
- Industrial Works Ltd

All four customers had relatively high consumption combined with renewable energy share below 15%.

---

## Business Recommendations

Based on the analysis, the following recommendations and areas for further investigation were identified:

### 1. Promote Energy Efficiency

Energy-efficiency initiatives should be considered for customers with high electricity consumption, particularly large industrial and business users.

### 2. Prioritize High-Attention Customers

The four customers identified by the high-attention rule could be prioritized for further investigation into energy efficiency and renewable-energy opportunities.

### 3. Investigate Low Renewable Shares

Large consumers with relatively low renewable-energy shares could be investigated to determine whether renewable-energy solutions could reduce dependence on conventional electricity sources.

### 4. Expand Cost Analysis

Future analysis could examine electricity costs by location and customer type to provide a clearer understanding of the financial impact of electricity consumption.

### 5. Improve Monthly Analysis

A longer period of customer-level data should be collected so that actual individual consumption patterns and seasonal changes can be studied more reliably.

### 6. Review the Attention Rule

The current high-attention rule could be refined using additional variables and real-world energy-sector criteria.

### 7. Expand the Dataset

A larger dataset containing more customers, locations, and time periods would provide stronger analytical insights.

---

## Limitations

This project has several limitations:

- The dataset contains only **20 records**.
- The dataset is simulated and does not represent official Nigerian utility or NERC statistics.
- Each customer appears only once across the six-month period, which limits the ability to analyze individual seasonal consumption patterns.
- The high-attention rule was created for this project and has not been validated against real utility-sector criteria.
- Although cost, payment status, and outage hours are included in the dataset, they were not analyzed in depth.
- The small dataset limits how broadly the findings can be generalized.

---

## Future Improvements

The system could be developed further by:

- Using a larger real-world dataset where appropriate data access is available.
- Extending the analysis to cover longer periods.
- Adding more customers and locations.
- Using **Pandas** for more advanced data manipulation.
- Adding data visualization and interactive dashboards.
- Performing deeper analysis of electricity costs.
- Analyzing payment status and outstanding payments.
- Performing deeper outage analysis.
- Comparing peak and total consumption.
- Improving the high-attention detection criteria.
- Adding automated reporting.
- Connecting the system to external datasets or databases.
- Developing a more advanced user interface.

---

## Python Concepts Used

The project demonstrates several fundamental Python programming concepts, including:

- Variables
- Lists
- Dictionaries
- Indexing
- Conditional statements
- `if`, `elif`, and `else`
- `for` loops
- `while` loops
- Nested loops
- Functions
- Parameters and arguments
- Return statements
- Data validation
- Basic calculations
- Dictionary-based grouping
- Menu-driven programming


### Main Menu

![Main Menu](screenshots/Screenshot%202.png)

### Data Validation

![Data Validation](./Screenshot%201.png)

### Consumption Analysis

![Consumption Analysis](./Screenshot%203.png)

### Cost Analysis

![Cost Analysis](./Screenshot%204.png)

### Location Analysis

![Location Analysis](./Screenshot%205.png)

### Customer Type Analysis

![Customer Type Analysis](./Screenshot%206.png)

### Monthly Analysis

![Monthly Analysis](./Screenshot%207.png)

### Consumption Classification

![Consumption Classification](./Screenshot%208.png)

### High-Attention Customers

![High-Attention Customers](./Screenshot%208.png)

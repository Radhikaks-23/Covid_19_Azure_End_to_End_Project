# Covid_19_Azure_End_to_End_Project

# Project Overview
This project is built around implementing a real-world data engineering solution using Azure Data Factory (ADF) to process and report COVID-19 trends and predict the virus's spread. The architecture follows a cloud-based approach, leveraging several Azure services to orchestrate, process, and store data, with reporting handled through Power BI.

# Source Data: 📤

Covid_19 Dataset- The COVID-19 data used in this project comes from various public APIs or data repositories that provide up-to-date data on cases, recoveries, deaths, and other related metrics. 

# Destination: 📥📍 Azure SQL database 

# Data Flow Overview:
Data Ingestion: ADF pipelines extract raw COVID-19 data from external sources such as public APIs or CSV Flat Files.
Data Transformation: The ingested data is cleaned, enriched, and processed using ADF pipelines and services like Azure Databricks or HDInsight.
Data Storage: Transformed data is stored in Azure Data Lake Storage, Blob Storage, or Azure SQL Database.
Reporting: Power BI is used to visualize and report COVID-19 trends based on the processed data stored in Azure SQL Database or other storage systems.

![image](https://github.com/user-attachments/assets/4eb14186-dec3-43b2-bd95-6ca6056d05b8)

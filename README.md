# COVID-19 Global Data Tracker

This project analyzes global COVID-19 data to visualize trends in cases, deaths, and vaccinations. It uses Python libraries like **pandas**, **matplotlib**, **seaborn**, and **plotly** for data processing and visualization.

## Project Overview:
- Clean and explore COVID-19 data
- Visualize trends in total cases, deaths, and vaccinations over time
- Compare key metrics like death rates and vaccination rates across countries

## Dataset:
The dataset used is from **Our World in Data**, which provides COVID-19 data for various countries. You can download the dataset from [this link](https://github.com/owid/covid-19-data/tree/master/public/data).

## Setup:
Before running the script, you need to install the required libraries. Run the following command to install them:

```bash
pip install pandas matplotlib seaborn plotly

How to Run:

    Download the owid-covid-data.csv file and place it in the same directory as the covid.py script.

    Run the Python script:

    python covid.py

Features:

    Line charts to visualize total cases and deaths over time

    Bar charts comparing total cases and deaths across countries

    Visualization of vaccination progress using line charts

    Optional choropleth map to show COVID-19 case density by country

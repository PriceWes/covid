import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# Load the dataset
def load_data(file_path):
    try:
        df = pd.read_csv(file_path)
        print(f"Dataset loaded successfully. First few rows:\n{df.head()}")
        return df
    except Exception as e:
        print(f"Error loading dataset: {e}")

# Explore and clean the dataset
def clean_data(df):
    # Filter countries of interest
    countries_of_interest = ['Kenya', 'USA', 'India']
    df_filtered = df[df['location'].isin(countries_of_interest)]
    
    # Convert 'date' column to datetime
    df_filtered['date'] = pd.to_datetime(df_filtered['date'])
    
    # Handle missing numeric values
    df_filtered['total_cases'] = df_filtered['total_cases'].fillna(0)
    df_filtered['total_deaths'] = df_filtered['total_deaths'].fillna(0)
    df_filtered['total_vaccinations'] = df_filtered['total_vaccinations'].fillna(0)
    
    print(f"Data after cleaning:\n{df_filtered.head()}")
    return df_filtered

# Exploratory Data Analysis (EDA)
def analyze_data(df):
    # Calculate basic statistics
    print("Basic statistics of the dataset:")
    print(df.describe())
    
    # Plot total cases over time
    plt.figure(figsize=(10, 6))
    sns.lineplot(x='date', y='total_cases', hue='location', data=df)
    plt.title('Total COVID-19 Cases Over Time')
    plt.xlabel('Date')
    plt.ylabel('Total Cases')
    plt.legend(title='Country')
    plt.show()

    # Plot total deaths over time
    plt.figure(figsize=(10, 6))
    sns.lineplot(x='date', y='total_deaths', hue='location', data=df)
    plt.title('Total COVID-19 Deaths Over Time')
    plt.xlabel('Date')
    plt.ylabel('Total Deaths')
    plt.legend(title='Country')
    plt.show()

    # Calculate death rate
    df['death_rate'] = df['total_deaths'] / df['total_cases']
    
    # Plot death rate comparison
    plt.figure(figsize=(10, 6))
    sns.barplot(x='location', y='death_rate', data=df)
    plt.title('COVID-19 Death Rate by Country')
    plt.xlabel('Country')
    plt.ylabel('Death Rate')
    plt.show()

# Visualizing vaccination progress
def visualize_vaccinations(df):
    # Plot cumulative vaccinations over time
    plt.figure(figsize=(10, 6))
    sns.lineplot(x='date', y='total_vaccinations', hue='location', data=df)
    plt.title('Cumulative Vaccinations Over Time')
    plt.xlabel('Date')
    plt.ylabel('Total Vaccinations')
    plt.legend(title='Country')
    plt.show()

    # Compare vaccination rate by country
    df['vaccination_rate'] = (df['total_vaccinations'] / df['population']) * 100
    
    plt.figure(figsize=(10, 6))
    sns.barplot(x='location', y='vaccination_rate', data=df)
    plt.title('Vaccination Rate by Country')
    plt.xlabel('Country')
    plt.ylabel('Vaccination Rate (%)')
    plt.show()

# Optional: Build a Choropleth Map
def choropleth_map(df):
    # Create a choropleth map of total cases by country (latest date)
    latest_data = df[df['date'] == df['date'].max()]
    fig = px.choropleth(latest_data, locations='iso_code', color='total_cases',
                        hover_name='location', color_continuous_scale='Viridis',
                        title="COVID-19 Total Cases by Country")
    fig.show()

# Main function to load, clean, analyze, and visualize the data
def main():
    # Load the dataset
    file_path = 'owid-covid-data.csv'  # Update the path as needed
    df = load_data(file_path)
    
    # Clean the data
    df_filtered = clean_data(df)
    
    # Perform data analysis and visualize
    analyze_data(df_filtered)
    
    # Visualize vaccination progress
    visualize_vaccinations(df_filtered)
    
    # Optional: Build choropleth map
    choropleth_map(df_filtered)

# Run the main function
if __name__ == '__main__':
    main()

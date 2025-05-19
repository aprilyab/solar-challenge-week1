import streamlit as st  # For building the web app
import seaborn as sns  # For creating the boxplot
import matplotlib.pyplot as plt  # For plotting
import pandas as pd  # For data manipulation
from utils import load_data
  # Custom function to load cleaned solar data

# Title of the dashboard
st.title("🌞 Cross-Country Solar Energy Dashboard")

# Load the combined dataset using the custom utility function
df = load_data()

# Sidebar widget for selecting one or more countries to filter the data
countries = st.multiselect(
    "Select Country/Countries",
    df['Country'].unique(),  # Available options (unique country names)
    default=df['Country'].unique()  # By default, all countries are selected
)

# Filter the dataset based on selected countries
filtered_df = df[df['Country'].isin(countries)]

# Dropdown menu for selecting which solar metric to analyze
metric = st.selectbox(
    "Select Solar Metric",
    ['GHI', 'DNI', 'DHI']  # Common solar radiation metrics
)

# Create a boxplot to show distribution of the selected metric across countries
st.subheader(f"Distribution of {metric} by Country")
fig, ax = plt.subplots()
sns.boxplot(
    x='Country',
    y=metric,
    data=filtered_df,
    ax=ax,
    palette='Set2'  # Color palette for better visual appeal
)
st.pyplot(fig)  # Display the plot in the app

# Display a table of top 5 regions with the highest average value for the selected metric
st.subheader(f"Top 5 Regions by Average {metric}")
top_regions = (
    filtered_df
    .groupby(['Country', 'region'])[metric]  # Group by country and region
    .mean()  # Calculate mean metric value
    .reset_index()  # Convert back to DataFrame
)
top_5 = top_regions.sort_values(by=metric, ascending=False).head(5)  # Get top 5 regions
st.table(top_5)  # Display the results in a table format

import streamlit as st  # Streamlit library to build interactive web apps
import seaborn as sns  # For creating attractive statistical plots
import matplotlib.pyplot as plt  # For plotting graphs
from utils import load_data
  # Import the custom function to load solar data

# Title displayed at the top of the Streamlit app
st.title("Cross-Country Solar Energy Dashboard")

# Load the combined solar dataset using the utility function
df = load_data()

# Sidebar multi-select widget for users to pick countries to filter data by
countries = st.multiselect(
    "Select Country/Countries",
    df['Country'].unique(),       # Options: unique country names
    default=df['Country'].unique()  # Default: all countries selected
)

# Filter the data to only include rows matching the selected countries
filtered_df = df[df['Country'].isin(countries)]

# Dropdown menu for selecting a solar metric to analyze
metric = st.selectbox(
    "Select Solar Metric",
    ['GHI', 'DNI', 'DHI']  # Common solar radiation metrics
)

# Display a subheader for the boxplot section
st.subheader(f"Distribution of {metric} by Country")

# Create a matplotlib figure and axes for the boxplot
fig, ax = plt.subplots()

# Use seaborn to create a boxplot of the selected metric by country
sns.boxplot(
    x='Country',
    y=metric,
    data=filtered_df,
    ax=ax,
    palette='Set2'  # Color palette for improved visuals
)

# Render the boxplot figure in the Streamlit app
st.pyplot(fig)

# Display a subheader for the top countries table (since region column is missing)
st.subheader(f"Top 3 Countries by Average {metric}")

# Group the filtered data by 'Country' only (since 'region' does not exist)
top_countries = (
    filtered_df
    .groupby('Country')[metric]  # Group by country and select the metric column
    .mean()                     # Calculate mean for each country
    .reset_index()              # Reset index to make 'Country' a column again
)

# Sort countries by descending metric value and select the top 5
top_5 = top_countries.sort_values(by=metric, ascending=False).head(5)

# Display the top 5 countries as a table in the app
st.table(top_5)

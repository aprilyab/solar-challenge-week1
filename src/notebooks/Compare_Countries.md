# Cross-Country Solar Potential Comparison

## Overview
This project analyzes and compares solar radiation metrics — Global Horizontal Irradiance (GHI), Direct Normal Irradiance (DNI), and Diffuse Horizontal Irradiance (DHI) — across three countries: **Benin**, **Togo**, and **Sierra Leone**. The goal is to identify differences in solar potential and provide actionable insights to guide solar energy planning.

---

## Data

- Cleaned CSV files for each country located in the `data/` folder:
  - `benin_clean.csv`
  - `togo_clean.csv`
  - `sierraleone_clean.csv`

Each dataset contains hourly/daily solar radiation metrics and has been cleaned and prepared for analysis.

---

## Process Overview

### 1. Data Loading and Preparation

- Load each country’s cleaned CSV file into a Pandas DataFrame.
- Add a `Country` column to identify the data source.
- Concatenate all three datasets into a single DataFrame for unified analysis.

### 2. Exploratory Data Analysis (EDA)

- Generate boxplots for each metric (GHI, DNI, DHI), comparing distributions side-by-side across countries.
- Calculate summary statistics (mean, median, standard deviation) for each metric by country.

### 3. Statistical Testing

- Conduct a one-way ANOVA test on GHI to assess if the differences between countries are statistically significant.
- Report the resulting p-value with appropriate formatting.

### 4. Visual Summary

- Create a bar chart ranking countries by average GHI to visually highlight solar potential.

### 5. Key Observations

- Summarize insights such as variability in GHI, stability in DNI, and statistical significance of differences.

---

## Key Performance Indicators (KPIs)

- **Inclusion of all three countries in each plot** to allow direct comparison.
- **Correct implementation and reporting of p-values** from statistical tests.
- **Relevance and actionability of insights** derived from the data.
- **Use of a summary table** comparing mean, median, and standard deviation for each metric.

---

## Example Code Snippets

```python
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import f_oneway

# Load data
benin = pd.read_csv('data/benin_clean.csv')
togo = pd.read_csv('data/togo_clean.csv')
sierra = pd.read_csv('data/sierraleone_clean.csv')

# Add Country column
benin['Country'] = 'Benin'
togo['Country'] = 'Togo'
sierra['Country'] = 'Sierra Leone'

# Combine datasets
df = pd.concat([benin, togo, sierra], ignore_index=True)

# Summary statistics
metrics = ['GHI', 'DNI', 'DHI']
summary = df.groupby('Country')[metrics].agg(['mean', 'median', 'std']).round(2)
print(summary)

# Boxplot for GHI
sns.boxplot(x='Country', y='GHI', data=df, palette='Set2')
plt.title("Boxplot of GHI by Country")
plt.show()

# One-way ANOVA test for GHI
f_stat, p_val = f_oneway(
    df[df['Country'] == 'Benin']['GHI'],
    df[df['Country'] == 'Togo']['GHI'],
    df[df['Country'] == 'Sierra Leone']['GHI']
)
print(f"ANOVA p-value for GHI comparison: {p_val:.4f}")

# Bar chart ranking countries by average GHI
avg_ghi = df.groupby('Country')['GHI'].mean().sort_values(ascending=False)
sns.barplot(x=avg_ghi.index, y=avg_ghi.values, palette='viridis')
plt.title("Average GHI by Country")
plt.ylabel("GHI")
plt.xlabel("Country")
plt.show()

import pandas as pd  # Import the pandas library for data manipulation

# Function to load and combine cleaned data from multiple countries
def load_data():
    # Load cleaned CSV data files for each country into separate DataFrames
    benin = pd.read_csv('data/benin_clean.csv')
    togo = pd.read_csv('data/togo_clean.csv')
    sierra = pd.read_csv('data/sierraleone_clean.csv')

    # Add a 'Country' column to each DataFrame to identify the source
    benin['Country'] = 'Benin'
    togo['Country'] = 'Togo'
    sierra['Country'] = 'Sierra Leone'

    # Concatenate the DataFrames into a single DataFrame
    # ignore_index=True ensures the index is reset
    df = pd.concat([benin, togo, sierra], ignore_index=True)
    
    # Return the combined DataFrame
    return df

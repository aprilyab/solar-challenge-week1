import pandas as pd  # Import pandas library for data manipulation
print("hhhg")
def load_data():
    # Load cleaned CSV data files for each country from the specified directory
    benin = pd.read_csv('data/benin_clean.csv')
    togo = pd.read_csv('data/togo_clean.csv')
    sierra = pd.read_csv('data/sierraleone_clean.csv')


# Temporary comment to test git change detection

    # Add a new column 'Country' to each DataFrame to identify the data source
    benin['Country'] = 'Benin'
    togo['Country'] = 'Togo'
    sierra['Country'] = 'Sierra Leone'

    # Combine all country DataFrames into one DataFrame
    # ignore_index=True resets the row index in the combined DataFrame
    df = pd.concat([benin, togo, sierra], ignore_index=True)
    
    # Return the combined DataFrame for further use
    return df


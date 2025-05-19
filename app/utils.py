import pandas as pd  # Import pandas library for data manipulation

def load_data():
    # Load cleaned CSV data files for each country from the specified directory
    benin = pd.read_csv('C:/Users/user/Desktop/solar-challenge-week1/src/notebooks/data/benin_clean.csv')
    togo = pd.read_csv('C:/Users/user/Desktop/solar-challenge-week1/src/notebooks/data/togo_clean.csv')
    sierra = pd.read_csv('C:/Users/user/Desktop/solar-challenge-week1/src/notebooks/data/sierraleone_clean.csv')




    # Add a new column 'Country' to each DataFrame to identify the data source
    benin['Country'] = 'Benin'
    togo['Country'] = 'Togo'
    sierra['Country'] = 'Sierra Leone'

    # Combine all country DataFrames into one DataFrame
    # ignore_index=True resets the row index in the combined DataFrame
    df = pd.concat([benin, togo, sierra], ignore_index=True)
    
    # Return the combined DataFrame for further use
    return df


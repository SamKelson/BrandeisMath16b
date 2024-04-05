# %%
import pandas as pd

# %%
def get_per_cap_gdp(file_path: str) -> pd.DataFrame:
    """
    Calculates the per capita gdp for countries in the given file.

    Args:
        file_path (str): The path to the file containing the country data.

    Returns:
        pd.DataFrame: new DataFrame that has two columns: “Country Name” and “Per-Capita GDP”.
    """

    # Read the data from the file
    data = pd.read_csv(file_path)

    # Create a new DataFrame with the required columns
    df = pd.DataFrame()
    df['Country Name'] = data['Country Name']
    df['Per-Capita GDP'] = data['GDP'] / data['Population']

    return df

# %%
def get_emissions_sum(file_path: str, L1: 'list[str]', L2: 'list[str]') -> float:
    """
    Calculates the sum of emissions for the given countries and years.

    Args:
        file_path (str): The path to the file containing the emissions data.
        L1 (list): A list of country names.
        L2 (list): A list of years.

    Returns:
        float: The sum of emissions for the specified countries and years.
    """

    # Read the data from the file
    data = pd.read_csv(file_path)

    #create a new column with the specifcs year columns summed
    data['specificSum'] = data[L2].sum(axis=1)
    #return the sum of the specific countries
    return data[data['Country Name'].isin(L1)]['specificSum'].sum()

# %%
def get_total_volume(file_path:str, year:str) -> float:
    """
    Calculates the total volume of a stock in given year from a file.

    Args:
        file_path (str): The path to the file containing the data.
        year (str): The year for which to calculate the total stock volume.

    Returns:
        float: The total stock volume for the given year.
    """
    
    # Read the data from the file
    data = pd.read_csv(file_path)
    data = data[['Date','Volume']]

    # Convert the 'Date' column to datetime object in format='%Y-%m-%d'
    data['Date'] = pd.to_datetime(data['Date'], format='%Y-%m-%d')

    # Extract the year from the 'Date' column using the datetime object
    data['Year'] = data['Date'].dt.year

    # Group the data by year and sum the values
    year_data = data.groupby('Year').sum(numeric_only=True)

    return year_data.loc[int(year)]['Volume']

# %%
def get_max_price(file_path: str) -> pd.DataFrame:
    """
    Reads a file containing price data on winery in various countries and returns a DataFrame with a list of countries and their most expensive winery.

    Parameters:
    file_path (str): The path to the file containing the price data.

    Returns:
    pd.DataFrame: A DataFrame with a list of countries and their most expensive winery.
    """
    
    # Read the data from the file
    data = pd.read_csv(file_path)

    # Drop rows with missing values in 'country' and 'price' columns
    data = data.dropna(subset=['country', 'price'])

    # Group by country and find the index of the maximum price in each group
    idx = data.groupby('country')['price'].idxmax()

    # Use the index to select the rows in original dataframe with the maximum price in each country and return selection with the name of winery and country and reset the index
    return data.loc[idx][['country', 'winery']].groupby('country').sum()
    

# %%
def min_weight(file_path:str) -> pd.DataFrame:
    """
    Finds the name and origin of the car with minimum weight for each year from a given file.

    Parameters:
    file_path (str): The path to the file containing the weight data.

    Returns:
    pd.DataFrame: A DataFrame  whose index consists a list of years, and which has
    two columns: name and origin, which gives the name and the origin of the car
    made in that year with the smallest weight.
    """
    
    # Read the data from the file
    data = pd.read_csv(file_path)

    # Group by year and find the index of the min weight in each group
    idx = data.groupby('year')['weight'].idxmin()

    #fix indexing to the year of car
    df = data.loc[idx][['name', 'origin']]
    df = df.set_index(idx.index,drop=True)
    df.index.name = None
    return df    

import pandas as pd

def load_data():
    # Load the historical game data
    df = pd.read_csv('data/raw/historical_data.csv')
    print(df.columns)  # Print column names to inspect the data
    print(df.head())  # Print first few rows of the dataframe
    return df

if __name__ == '__main__':
    df = load_data()

import pandas as pd

def load_data():
    # Load the historical game data
    df = pd.read_csv('data/raw/historical_data.csv')
    return df

def clean_data(df):
    # Handle missing values
    df.fillna(0, inplace=True)
    # Convert data types if necessary
    # Example: df['column_name'] = df['column_name'].astype(int)
    return df

def feature_engineering(df):
    # Example feature: rolling average of points scored by a team in the last 5 games
    df['team_points_last_5'] = df.groupby('TEAM_ID')['PTS'].transform(lambda x: x.rolling(window=5).mean())
    # Create other relevant features
    # Example: Home/Away feature
    df['home_game'] = df['MATCHUP'].apply(lambda x: 1 if 'vs.' in x else 0)

    return df

def preprocess_data():
    # Load the data
    df = load_data()
    # Clean the data
    df = clean_data(df)
    # Feature engineering
    df = feature_engineering(df)
    # Save the processed data
    df.to_csv('data/processed/preprocessed_historical_data.csv', index=False)
    print("Data preprocessing complete. Processed data saved to data/processed/preprocessed_historical_data.csv")

def main():
    preprocess_data()

if __name__ == '__main__':
    main()

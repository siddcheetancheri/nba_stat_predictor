from nba_api.stats.endpoints import leaguegamefinder
import pandas as pd
from datetime import datetime

def get_current_season():
    current_year = datetime.now().year
    current_month = datetime.now().month
    if current_month >= 10:  # From October to December, we are in the new season of the current year
        season_start_year = current_year
        season_end_year = current_year + 1
    else:  # From January to June, we are in the continuation of the previous season
        season_start_year = current_year - 1
        season_end_year = current_year
    return f"{season_start_year}-{str(season_end_year)[-2:]}"

def fetch_historical_data():
    season = get_current_season()
    print(f"Fetching data for the {season} season")
    gamefinder = leaguegamefinder.LeagueGameFinder(season_nullable=season)
    games = gamefinder.get_data_frames()[0]
    games.to_csv('data/raw/historical_data.csv', index=False)
    print("Historical data fetched and saved to data/raw/historical_data.csv")

def main():
    fetch_historical_data()

if __name__ == '__main__':
    main()

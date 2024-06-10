## Data Collection

To collect and preprocess the data, follow these steps:

1. **Set up the environment**:
    - Create a virtual environment and install the dependencies:
      ```sh
      python -m venv venv
      source venv/bin/activate  # On Windows use `venv\Scripts\activate`
      pip install -r requirements.txt
      ```

2. **Collect the data**:
    - Run the data collection script to fetch historical game data:
      ```sh
      python src/data_collection.py
      ```

3. **Preprocess the data**:
    - Run the preprocessing script to clean and prepare the data:
      ```sh
      python src/preprocessing.py
      ```

The preprocessed data will be saved to `data/processed/preprocessed_historical_data.csv`.
import pandas as pd
import numpy as np

from Global import * #file with all the config

for symbol in symbols:
    # Read the data from the CSV file
    data = pd.read_csv(f'DataFiles/{symbol.replace("/", "")}_data.csv', low_memory=False, encoding='utf-8', delimiter=';')
    print(data.columns)
    rowAtStart = data.size/len(data.columns)
    print(f" Number of rows before processing : {rowAtStart}")

    # Reverse the data so the oldest data is at the top
    data = data.iloc[::-1].reset_index(drop=True)

    # Calculate the moving averages
    data['avg_close_last_5'] = data['close'].rolling(window=5).mean()
    data['avg_close_last_10'] = data['close'].rolling(window=10).mean()
    data['avg_close_last_20'] = data['close'].rolling(window=20).mean()

    # Calculate the time since the last data point and convert it to seconds
    data['datetime'] = pd.to_datetime(data['datetime'])
    data['time_since_last_data'] = data['datetime'].diff().dt.total_seconds()

    # Drop the rows with NaN values in the moving average columns
    data = data.dropna(subset=['avg_close_last_5', 'avg_close_last_10', 'avg_close_last_20', 'time_since_last_data'])

    # Calculate a rolling window where all 'time_since_last_data' values are less than 60 seconds
    data['all_last_20_less_than_60sec'] = data['time_since_last_data'].rolling(window=20).apply(lambda x: np.all(x <= 60))

    # Keep only the rows where all 'time_since_last_data' values in the last 20 rows are less than 60 seconds
    data = data[data['all_last_20_less_than_60sec'] == 1.0]

    # Drop the 'all_last_20_less_than_60sec' column as it's no longer needed
    data = data.drop(columns=['all_last_20_less_than_60sec'])

    # Write the data to a new CSV file
    data.to_csv(f'ProcessedDataFiles/{symbol.replace("/", "")}_processed_data.csv', index=False, mode='w')
    rowAtEnd = data.size/len(data.columns)
    print(f"done with {symbol} with {rowAtEnd} rows at the end. Meaning {((rowAtStart-rowAtEnd)/rowAtStart)*100}% loss of data due to processing")

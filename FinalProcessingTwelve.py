import numpy as np
import pandas as pd
symbols=["USD/JPY"]

for symbol in symbols:
    # Load the data
    data = pd.read_csv(f'ProcessedDataFiles/{symbol.replace("/", "")}_processed_data.csv', low_memory=False, encoding='utf-8')

    # Calculate the time since the last data point and convert it to seconds
    data['datetime'] = pd.to_datetime(data['datetime'])
    data['time_since_last_data2'] = data['datetime'].diff().dt.total_seconds()
    # Drop the rows with NaN values in the moving average columns
    data = data.dropna(subset=['time_since_last_data2'])
    # Calculate a rolling window where all 'time_since_last_data' values are less than 60 seconds
    data['all_last_50_less_than_60sec'] = data['time_since_last_data'].rolling(window=50).apply(lambda x: np.all(x <= 60))
    # Keep only the rows where all 'time_since_last_data' values in the last 50 rows are less than 60 seconds


    # Select the columns you're interested in
    features = ['open', 'high', 'low', 'close', 'avg_close_last_5', 'avg_close_last_10', 'avg_close_last_20','all_last_50_less_than_60sec']
    data = data[features]

    # Convert the data to a numpy array
    data_array = data.values

    # Define the number of time steps in each sequence
    sequence_length = 50

    # Create a list to hold the sequences
    sequences = []

    # Create the sequences
    for i in range(sequence_length,len(data)):
        if data['all_last_50_less_than_60sec'][i] == 1.0 :
            sequence = data_array[i-sequence_length:i]
            sequences.append(sequence[:, :-1])

    # Convert the list of sequences into a numpy array
    sequences = np.array(sequences)
    np.save(f'FinalInputsFiles/FinalInputs{symbol.replace("/", "")}.npy', sequences)
    print(f'Done with {symbol} {len(sequences)}')

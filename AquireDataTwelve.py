# for greater simplicity install our package
    # https://github.com/twelvedata/twelvedata-python
import requests
import pandas as pd
from io import StringIO
import time
import requests

api_keys = ["YourAPIkey"]
interval = '1min'
symbols=['USD/JPY']
startDates = ["2023-07-19 8:30:00"]
endDates = ["2023-07-19 18:20:00"]
key_index = 0


def get_intraday_extended_data(symbol, interval, start_date, end_date, api_key):
    base_url = "https://api.twelvedata.com/time_series?"
    # Define the parameters for the request
    params = {
        "symbol": symbol,
        "interval": interval,
        "start_date" : start_date,
        "end_date" : end_date,
        "apikey": api_key,
        "format": "CSV",
        "previous_close" : "true"
    }

    response = requests.get(base_url, params=params)
    print(response)

    #response = requests.get("https://api.twelvedata.com/time_series?apikey="+api_key+"&interval="+interval+"&symbol="+symbol+"&dp=4&"+slice+"&previous_close=true")
    if response.status_code == 200:
        data = pd.read_csv(StringIO(response.text))
        print(data)
        return data
    else:
        raise Exception(f"Request failed with status {response.status_code}")


# Loop over all symbols
for symbol in symbols:

    # Create an empty DataFrame to store all data for this symbol
    data_all = pd.DataFrame()

    # Loop over all slices
    for idx in range(len(startDates)):
        start = time.time()
        # Get the data for this slice
        data = get_intraday_extended_data(symbol, interval, startDates[idx], endDates[idx], api_keys[key_index])
        finish = time.time()
        total = finish - start
        #print(total)

        # Append the data to the DataFrame
        data_all = pd.concat([data_all, data])

        # Increment the key index and reset it to 0 if it's out of range
        key_index += 1
        if key_index >= len(api_keys):
            key_index = 0

        # Sleep for a while to avoid hitting rate limits
        time.sleep(max(13-int(total),0))  # Adjust this value as needed

        print(f'slice just aquired :{symbol} : {startDates[idx], endDates[idx]} : {data.size} : {total}')

    # Save the data to a CSV file
    data_all.to_csv(f'DataFiles/{symbol.replace("/", "")}_data.csv', index=False)

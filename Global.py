import pandas as pd
from datetime import datetime, timedelta
api_keys = ["YourAPIKEY"]
MaxAPICallPerMin = 8 #even if you have 10 API keys the number of APIcall per min is the same but the total amount per day is increased
interval = '1min'
symbols=['USD/JPY']
startDate = ["2023-07-14 8:30:00"]
endDate = ["2023-07-19 18:20:00"]
columnsToKeepForRender = ['open', 'high', 'low', 'close'] #do not touch unless you know
# Select the columns you're interested in
columnsToKeep = ['open', 'high', 'low', 'close', 'avg_close_last_5', 'avg_close_last_10', 'avg_close_last_20']



# Convert start and end dates to datetime objects
start = pd.to_datetime(startDate)
end = pd.to_datetime(endDate)

# Calculate the time delta based on the interval
delta = pd.Timedelta(interval)
startDates = []
endDates = []
# Generate slices with the specified interval
current = start-delta
while current < end:
    current += delta
    startDates.append(current)
    current += delta * 5000
    endDates.append(min(current, end))

# Convert lists to desired format, if needed
#startDates = [str(date) for date in startDates]
#endDates = [str(date) for date in endDates]
# Print the lists
#print("Start Dates:")
#print(startDates)
#print("\nEnd Dates:")
#print(endDates)
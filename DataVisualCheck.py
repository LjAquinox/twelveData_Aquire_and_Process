import pandas as pd
import mplfinance as mpf
import numpy as np
from datetime import datetime, timedelta
import random
from Global import * #file with all the config
random_symbol = random.choice(symbols).replace("/", "")


data = np.load('FinalInputsFiles/FinalInputs'+random_symbol+'.npy')
for i in range(100,500000,5):
    sequence = data[i]

    # Create a DataFrame
    df = pd.DataFrame(sequence, columns=columnsToKeep)

    # Keep only the columns needed for the candlestick plot
    df = df[columnsToKeepForRender]

    # Create a DatetimeIndex
    date_today = datetime.now()
    days = pd.date_range(date_today, date_today + timedelta(49), freq='D')

    # Set the index of the DataFrame to this DatetimeIndex
    df.index = days

    # Create a candlestick plot
    mpf.plot(df, type='candle', style='charles', title=random_symbol, ylabel='Price ($)')

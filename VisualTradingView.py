import websocket
import json
import datetime
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Variables for storing data
timestamps = []
prices = []


class StockData:
    def __init__(self):
        self._high = None
        self._low = None
        self._current = None

    def _update_data(self, price):
        self._current = price

        if self._high is None or price > self._high:
            self._high = price

        if self._low is None or price < self._low:
            self._low = price

    def get_current_price(self):
        return self._current

    def get_high_price(self):
        return self._high

    def get_low_price(self):
        return self._low

# WebSocket event: When the connection is established
def on_open(ws):
    print('WebSocket connection established')

    # Subscription message
    subscribe_message = {
        "action": "subscribe",
        "params": {
            "symbols": "USD/JPY"
        }
    }

    # Sending the subscription message
    ws.send(json.dumps(subscribe_message))

last_point = StockData()
# WebSocket event: When a message is received
def on_message(ws, message):
    data = json.loads(message)
    if "price" in data:
        price = data["price"]
        timestamp = data["timestamp"]
        #last_point._update_data #for future idea

        # Convert timestamp to date and time
        datetime_obj = datetime.datetime.fromtimestamp(timestamp)
        formatted_time = datetime_obj.strftime('%H:%M:%S')

        # Display the price and formatted time
        print('Price:', price,' at', formatted_time)

        # Append the new data to the lists
        timestamps.append(timestamp)
        prices.append(price)

        # Update the plot
        Xs = np.arange(1, len(prices) + 1)
        #plt.ylim(bottom=last_point.get_low_price(), top=last_point.get_high_price())  # Set y-axis limits
        plt.clf()  # Clear the previous plot
        plt.plot(Xs, prices, 'b-')  # Plot the data
        plt.xlabel('Time')
        plt.ylabel('Price')
        plt.title('Price over Time')
        plt.grid(True)
        plt.ticklabel_format(useOffset=False)  # Disable scientific notation on y-axis
        plt.pause(0.01)  # Pause to allow the plot to be displayed


# WebSocket event: When an error occurs
def on_error(ws, error):
    print('WebSocket error:', error)


# WebSocket event: When the connection is closed
def on_close(ws):
    print('WebSocket connection closed')

apikey = "YourAPIKEY"
# Establish WebSocket connection
websocket.enableTrace(True)  # Enable this line for debugging purposes
ws = websocket.WebSocketApp(
    'wss://ws.twelvedata.com/v1/quotes/price?apikey='+apikey,
    on_open=on_open,
    on_message=on_message,
    on_error=on_error,
    on_close=on_close
)

# Start WebSocket connection
ws.run_forever()
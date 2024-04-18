import requests
import matplotlib.pyplot as plt
from datetime import datetime
import time

def fetch_price():
    secret_key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJjbHVlIjoiNjYxOTViNjBmNWFmOTRlZWNlYWE1ZTQ3IiwiaWF0IjoxNzEyOTM3ODI0LCJleHAiOjMzMjE3NDAxODI0fQ.OEple4xZYvIByHpi63p_BMzOa0hOdrwVbUxja9kW3uY"
    response = requests.get(url=f"https://api.taapi.io/sma?secret={secret_key}&exchange=binance&symbol=BTC/USDT&interval=1h")
    return response.json()['value']

# Initialize lists to store timestamps and prices
timestamps = []
prices = []

# Function to update the plot
def update_plot():
    plt.clf()  # Clear previous plot
    plt.plot(timestamps, prices, marker='o', linestyle='-')
    plt.xlabel('Time')
    plt.ylabel('price')
    plt.title(f'BTC/USDT')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.pause(0.1)

# Main loop to fetch data every 15 seconds and update the plot
while True:
    try:
        price = fetch_price()
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        timestamps.append(timestamp)
        prices.append(price)

        
        # Keep only the last 10 data points for better visualization
        if len(timestamps) > 10:
            timestamps = timestamps[-10:]
            prices = prices[-10:]
        
        update_plot()
        time.sleep(15)  # Wait for 15 seconds before fetching the next price
    except KeyboardInterrupt:
        print("Exiting...")
        break

plt.show()  # Show the final plot

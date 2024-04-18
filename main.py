import requests

import time

def fetch_price():
    secret_key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJjbHVlIjoiNjYxOTViNjBmNWFmOTRlZWNlYWE1ZTQ3IiwiaWF0IjoxNzEyOTM3ODI0LCJleHAiOjMzMjE3NDAxODI0fQ.OEple4xZYvIByHpi63p_BMzOa0hOdrwVbUxja9kW3uY"
    response = requests.get(url=f"https://api.taapi.io/sma?secret={secret_key}&exchange=binance&symbol=BTC/USDT&interval=1h")
    return response.json()['value']

# Initialize lists to store timestamps and prices

while(True):
    print(fetch_price())
    for i in range(15):
        print(i)
        time.sleep(1)

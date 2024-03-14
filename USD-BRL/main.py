import requests, time
import json
import matplotlib.pyplot as plt
from datetime import datetime

link = "https://economia.awesomeapi.com.br/json/daily/USD-BRL/5"
r = requests.get(link)
data = r.json()
# print(data)

timestamps =[]
highs = []
lows = []
for entry in data:
    timestamps.append(datetime.fromtimestamp(int (entry['timestamp'])).strftime('%Y-%m-%d'))
    highs.append(float(entry['high']))
    lows.append(float(entry['low']))
    

plt.plot(timestamps, highs, label='High', marker='o', color='red')
plt.plot(timestamps, lows, label='Low', marker='o', color='green')

plt.xlabel('Date')
plt.ylabel('Price')
plt.title('USD-BRL')
plt.xticks(rotation=45)
plt.legend()

plt.tight_layout()
plt.show()
print(r.json()[0])
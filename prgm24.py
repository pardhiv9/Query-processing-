import matplotlib.pyplot as plt
from datetime import datetime
data = [
{"Date": "10-03-16", "Open": 774.25, "High": 776.065002, "Low": 769.5, "Close": 772.559998},
{"Date": "10-04-16", "Open": 776.030029, "High": 778.710022, "Low": 772.890015, "Close": 776.429993},
{"Date": "10-05-16", "Open": 779.309998, "High": 782.070007, "Low": 775.650024, "Close": 776.469971},
{"Date": "10-06-16", "Open": 779, "High": 780.47998, "Low": 775.539978, "Close": 776.859985}, {"Date": "10-07-16", "Open":779.659973, "High": 779.659973, "Low": 770.75, "Close": 775.080017}]
dates = [datetime.strptime(entry["Date"], "%m-%d-%y") for entry in data]
close_prices = [entry["Close"] for entry in data]
plt.figure(figsize=(10,5))
plt.plot(dates, close_prices, marker='o', linestyle='-')
plt.xlabel('Date')
plt.ylabel('Close Price (USD)')
plt.title('Alphabet Inc. Financial Data (Oct 3, 2016 to Oct 7, 2016)')
plt.gcf().autofmt_xdate()
plt.show()

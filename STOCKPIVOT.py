import matplotlib.pyplot as plt

# Define the ticker symbol and timeframe
ticker_symbol = 'AAPL'
start_date = '2023-01-01'
end_date = '2024-01-01'

# Fetch historical price data
stock_data = yf.download(ticker_symbol, start=start_date, end=end_date)

ef calculate_pivot_points(high, low, close):
    pivot = (high + low + close) / 3
    support1 = (2 * pivot) - high
    resistance1 = (2 * pivot) - low
    support2 = pivot - (high - low)
    resistance2 = pivot + (high - low)
    return pivot, support1, resistance1, support2, resistance2

# Assuming 'stock_data' contains Open, High, Low, Close prices
pivot, support1, resistance1, support2, resistance2 = calculate_pivot_points(
    stock_data['High'],
    stock_data['Low'],
    stock_data['Close']
)

print("Pivot Point:", pivot[-1])
print("Support 1:", support1[-1])
print("Resistance 1:", resistance1[-1])
print("Support 2:", support2[-1])
print("Resistance 2:", resistance2[-1])

# Plotting Pivot Points
plt.figure(figsize=(10, 6))
plt.plot(stock_data.index, stock_data['Close'], label='Close Price')
plt.axhline(y=pivot[-1], color='r', linestyle='--', label='Pivot')
plt.axhline(y=support1[-1], color='g', linestyle='--', label='Support 1')
plt.axhline(y=resistance1[-1], color='b', linestyle='--', label='Resistance 1')
plt.title('Pivot Points')
plt.xlabel('Date')
plt.ylabel('Price')
plt.legend()
plt.show()
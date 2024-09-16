import yfinance as yf

# Fetch GameStop stock data
gme_data = yf.download('GME', start='2020-01-01', end='2024-01-01')

# Reset the index of the dataframe
gme_data.reset_index(inplace=True)

# Save the dataframe to a CSV file
gme_data.to_csv('gme_data.csv', index=False)

# Display the first five rows
print(gme_data.head())

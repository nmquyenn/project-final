import yfinance as yf

# Fetch Tesla stock data
tesla_data = yf.download('TSLA', start='2020-01-01', end='2024-01-01')

# Reset the index of the dataframe
tesla_data.reset_index(inplace=True)

# Save the dataframe to a CSV file
tesla_data.to_csv('tesla_data.csv', index=False)

# Display the first five rows
print(tesla_data.head())

import pandas as pd

# Example code, replace with your actual scraping code
tesla_revenue = pd.read_csv('tesla_revenue.csv')

# Display the last five rows
print(tesla_revenue.tail())



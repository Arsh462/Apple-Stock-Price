# Apple-Stock-Price
This is a test case

In this project I fetched apple stock price using yfinance library to make a line chart of the historical closing prices of the apple stock between the period "2025-02-10" to "2026-02-10".

fetch_prices.py includes the code to fetch stock price with only date and close (USD) and the output data is stored as json in the file historicalPrices.json.
chart.py fetches the data from the json file (historicalPrices.json) to create a line chart and it is automatically saved as chart.png.



import yfinance as yf
import pandas as pd

try:
    ticker = "AAPL"
    data = yf.download(ticker, start="2025-02-10", end="2026-02-10")

    if data.empty:
        raise ValueError("No data retrieved. Check ticker symbol or date range.")

    # Flatten columns
    if isinstance(data.columns, pd.MultiIndex):
        data.columns = [col[0] for col in data.columns] 
    
    data.reset_index(inplace=True)

    
    df_filtered = data[['Date', 'Close']]

    # Converts date to string 
    df_filtered['Date'] = df_filtered['Date'].dt.strftime('%Y-%m-%d')

    # Convert to JSON  
    json_data = df_filtered.to_json(orient="records")

    # Save to file
    with open("historicalPrices.json", "w") as f:
        f.write(json_data)

    print("JSON file created successfully: historicalPrices.json")

except Exception as e:
    print(f"Error: {e}")


























        

        

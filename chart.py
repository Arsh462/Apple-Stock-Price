import json
import matplotlib.pyplot as plt
import os
import sys
from datetime import datetime

def load_json(file_path):
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File '{file_path}' not found.")

    with open(file_path, 'r') as file:
        try:
            data = json.load(file)
        except json.JSONDecodeError as e:
            raise ValueError(f"Invalid JSON format: {e}")

    if not isinstance(data, list):
        raise TypeError("JSON root must be a list of objects.")

   
    for entry in data:
        if not isinstance(entry, dict):
            raise TypeError("Each item in JSON must be an object.")
        if "Date" not in entry or "Close" not in entry:
            raise KeyError("Each object must contain 'Date' and 'Close' keys.")
        
    return data

def plot_line_chart(data, output_file):
    # line chart
    dates = []
    closes = []
    for entry in data:
        try:
            dates.append(datetime.strptime(entry["Date"], "%Y-%m-%d"))
            closes.append(float(entry["Close"]))
        except ValueError as e:
            raise ValueError(f"Invalid data format: {e}")

    plt.figure(figsize=(10, 10))
    plt.plot(dates, closes, marker='o', linestyle='-', color='b', label='Sales')
    plt.title("Apple (AAPL) - Historical Close Prices (Last Year)")
    plt.xlabel("Date")
    plt.ylabel("Close (USD)")
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.legend()
    plt.tight_layout()
    plt.savefig(output_file, format='png', dpi=300)  
    print(f"Chart saved as '{output_file}'")
    plt.show()

if __name__ == "__main__":
    try:
        json_file = "historicalPrices.json"  
        data = load_json(json_file)
        plot_line_chart(data, output_file = "chart.png")
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)

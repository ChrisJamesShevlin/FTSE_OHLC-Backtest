# MySQL FTSE Data Trade Profit Calculator

This repository contains a Python script that connects to a **MySQL database** containing FTSE stock data, identifies potential trading signals, and calculates the total profit or loss based on these trades. The script implements a simple strategy where a "buy" signal is generated when the current open price is higher than the previous low, and the "sell" occurs 10 minutes after the buy.

## Table of Contents

- [Overview](#overview)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Strategy Explanation](#strategy-explanation)
- [Customization](#customization)
- [License](#license)

## Overview

The script performs the following operations:
1. Connects to a **MySQL** database using the provided connection details.
2. Retrieves stock price data from a table (ordered by timestamp).
3. Evaluates potential trades based on a simple strategy.
4. Calculates the profit or loss by "buying" when the current open price is higher than the previous low and "selling" after 10 minutes.
5. Outputs the total profit or loss from the trades.

## Prerequisites

To run the script, you will need:
- A MySQL database running locally or remotely with FTSE data.
- A table containing stock data with at least the following columns:
  - Timestamp (ordered by time)
  - Open price
  - Low price
  - Close price
- Python 3 installed on your machine.
- The `mysql-connector-python` library for connecting to the MySQL database.

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/ftse-trade-profit-calculator.git
   cd ftse-trade-profit-calculator
   ```

2. **Install the required Python dependencies**:
   Install the MySQL connector for Python:
   ```bash
   pip install mysql-connector-python
   ```

3. **Set up the MySQL Database**:
   Make sure you have a MySQL database running, and the necessary table containing FTSE stock data is set up. The script expects the table to have columns for `timestamp`, `open`, `low`, and `close`.

## Usage

1. **Update the MySQL connection details**:
   In the script, update the following placeholders with your actual MySQL server details:

   ```python
   mydb = {
       'host': 'localhost',        # MySQL server host
       'user': 'root',             # MySQL user
       'password': '********',    # MySQL password
       'database': 'ftse_data',    # Name of your database
   }
   ```

2. **Update the table name**:
   Replace `tableName` in the SQL query with the actual table name that contains the FTSE stock data:
   ```python
   query = "SELECT * FROM tableName ORDER BY timestamp"
   ```

3. **Run the script**:
   Execute the script to connect to the MySQL database, fetch the rows, and calculate the total profit or loss:
   ```bash
   python ftse_trade_profit_calculator.py
   ```

### Example Output:
```bash
Total profit/loss from the trades: £512.30
```

## Strategy Explanation

The script identifies potential trades using the following logic:
- **Buy Signal**: If the current open price is higher than the previous low price, the script treats this as a buy signal.
- **Sell Signal**: The sell occurs after 10 minutes (or 10 rows later in the data).
- **Profit Calculation**: The profit is calculated as the difference between the close price (after 10 minutes) and the buy price. This profit (or loss) is then added to the total profit.

The strategy can be modified or enhanced depending on your needs.

## Customization

1. **Change the Profit Calculation Strategy**:
   You can modify the logic in the `find_trades_and_calculate_profit` function to implement your own trading strategy. For example, you could change the buy or sell conditions, or adjust the timeframe for the sell signal.

   ```python
   current_open = rows[i][2]  # Open price is the 3rd column
   previous_low = rows[i-1][4] if i > 0 else rows[i][4]  # Low price is the 5th column
   ```

2. **Modify the Sell Timeframe**:
   By default, the script assumes that the sell happens 10 minutes (or 10 rows) after the buy. You can change this to any number of rows:

   ```python
   sell_price = rows[i+10][5]  # Close price 10 minutes later (adjust the index as needed)
   ```

3. **Add Additional Logging**:
   You can add more detailed logging or print statements to track individual trades, profits, or losses for each trade.

## License

This project is licensed under the MIT License. See the [LICENSE](./LICENSE) file for more details.

---

This script provides a simple framework for calculating trading profits based on historical FTSE stock data from a MySQL database. Feel free to modify the logic to match your own trading strategy or data structure.

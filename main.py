import mysql.connector
from datetime import datetime, timedelta

mydb = {
    'host': 'localhost',
    'user': 'root',
    'password': 'Uia86w!md',
    'database': 'ftse_data',
}

# Function to find trades and calculate profit or loss
def find_trades_and_calculate_profit(rows):
    total_profit = 0
    for i in range(len(rows) - 10):
        current_open = rows[i][2]  # Open price is the 3rd column
        previous_low = rows[i-1][4] if i > 0 else rows[i][4]  # Low price is the 5th column, handle for first row
        
        # If the open price is higher than the previous low price, consider it a buy signal
        if current_open > previous_low:
            buy_price = current_open
            sell_price = rows[i+10][5]  # Close price 10 minutes later is the 6th column
            profit = sell_price - buy_price
            total_profit += profit
    
    return total_profit

# Main script
try:
    # Establish a connection to the MySQL database
    connection = mysql.connector.connect(**mydb)
    
    # Create a cursor object to execute SQL queries
    cursor = connection.cursor()
    
    # Execute a simple SELECT query to retrieve all data from the specified table
    query = "SELECT * FROM tableName ORDER BY timestamp"  # Make sure data is ordered by timestamp
    cursor.execute(query)
    
    # Fetch all the rows from the result set
    rows = cursor.fetchall()
    
    # Calculate profit or loss from trades
    total_profit = find_trades_and_calculate_profit(rows)
    
    # Output the result
    print(f"Total profit/loss from the trades: £{total_profit}")

finally:
    # Close the cursor and connection
    if 'cursor' in locals():
        cursor.close()
    if 'connection' in locals():
        connection.close()

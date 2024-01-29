# Add your API KEY below

import requests
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter, YearLocator

# Your Etherscan API key
api_key = 'YOUR_API_KEY_HERE'

# Example Ethereum address
address = '0xba1951dF0C0A52af23857c5ab48B4C43A57E7ed1'

# Example API endpoint for getting transactions
endpoint = f'https://api.etherscan.io/api?module=account&action=txlist&address={address}&apikey={api_key}'

# Make a GET request to the API
response = requests.get(endpoint)

# Check if the request was successful (status code 200)
if response.status_code == 200:
   # Parse the JSON response
   data = response.json()
 
   # Check if the response contains transactions
   if data['status'] == '1':
       # Extract the list of transactions from the response
       transactions = data['result']
     
       # Create a DataFrame to store the transaction data
       tx_df = pd.DataFrame(transactions)
     
       # Convert 'timeStamp' to datetime format
       tx_df['timeStamp'] = pd.to_datetime(tx_df['timeStamp'], unit='s')
     
       # Convert 'value' from wei to Ether
       tx_df['value'] = tx_df['value'].astype(float) / 10**18
     
       # Convert 'gasUsed' to float
       tx_df['gasUsed'] = tx_df['gasUsed'].astype(float)
     
       # Calculate gas paid in Ether (gasUsed * gasPrice)
       tx_df['gasPrice'] = tx_df['gasPrice'].astype(float) / 10**18
       tx_df['gasPaid'] = tx_df['gasUsed'] * tx_df['gasPrice']
     
       # Plot: Account Time vs Ether(ETH) Value
       plt.figure(figsize=(10, 5))
       plt.plot(tx_df['timeStamp'], tx_df['value'], marker='o')
       plt.title(f'Transactions for Ethereum Address: {address}\nAccount Time vs Ether(ETH) Value')
       plt.xlabel('Time')
       plt.ylabel('Value (Ether)')
       plt.grid(True)
      
       # Customize x-axis tick format to display years
       date_format = DateFormatter("%Y")
       plt.gca().xaxis.set_major_formatter(date_format)
      
       # Set the tick locator to include all years
       plt.gca().xaxis.set_major_locator(YearLocator())
      
       plt.show()

       # Plot: Account Time vs Gas paid (in ETH)
       plt.figure(figsize=(10, 5))
       plt.plot(tx_df['timeStamp'], tx_df['gasPaid'], marker='o', color='r')
       plt.title(f'Transactions for Ethereum Address: {address}\nAccount Time vs Gas paid (in ETH)')
       plt.xlabel('Time')
       plt.ylabel('Gas paid (in ETH)')
       plt.grid(True)
      
       # Customize x-axis tick format to display years
       plt.gca().xaxis.set_major_formatter(date_format)
      
       # Set the tick locator to include all years
       plt.gca().xaxis.set_major_locator(YearLocator())
      
       plt.show()
   else:
       print('No transactions found for the address')
else:
   print('Failed to fetch data from the API:', response.status_code)

# Add your API KEY below

import requests
import json

def get_transaction_details(tx_hash, api_key):
   url = f"https://api.etherscan.io/api?module=proxy&action=eth_getTransactionByHash&txhash={tx_hash}&apikey={api_key}"
   response = requests.get(url)
   data = response.json()
   return data

def print_transaction_details(transaction):
   print(json.dumps(transaction, indent=4))

# Replace with your transaction hash and API key
transaction_hash = '0x0f0f23f081fb91b47334a678bda61be2b459b4f438762436e9a64d87791a257c'
api_key = 'YOUR_API_KEY_HERE'

transaction_details = get_transaction_details(transaction_hash, api_key)
print_transaction_details(transaction_details)

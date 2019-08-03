from __future__ import print_function
import time
import intrinio_sdk
from intrinio_sdk.rest import ApiException
from pprint import pprint
import json

intrinio_sdk.ApiClient().configuration.api_key['api_key'] = 'OjBhZTg1NmU4ZmJlNWZkOGE2YTgxOTVjZjgwYTA5ODIx'

security_api = intrinio_sdk.SecurityApi()

identifier = input('Please enter a ticker symbol: ').upper()
source = '' 

try:
  api_response = security_api.get_security_realtime_price(identifier, source=source)
except ApiException as e:
  print("Exception when calling SecurityApi->get_security_realtime_price: %s\r\n" % e)
    
last_price = api_response.last_price

print('Current Price Per Share:',last_price)
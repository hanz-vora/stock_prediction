import json
import requests
import alpha_vantage
from stocks.scripts.config import apikey as apikey

#Using Alpha Vantage API for real time stock/securities data
API_URL = "https://www.alphavantage.co/query"

#function to return single share price given a ticker symbol
#Using two seperate API requests, the user entered symbol is first searched and matched to an existing US or major global equity
#If there is a match, a second request is made for the corresponding share price
def curr_share_price(symbol):

  #Required data for SYMBOL SEARCH function, returns an object with array 'bestMatches' in csv,json,pandas
  extraData = {
      "function": "SYMBOL_SEARCH",
      "keywords": symbol,
      "outputsize": "compact",
      "datatype": "json",
      "apikey": apikey
  }

  #API call for SYMBOL SEARCH (MAX 5 requests per minute and 500 requests per day)
  responseName = requests.get(API_URL, params=extraData)

  #Create python dictionary with json data
  response_dict_two = json.loads(responseName.text)

  #parse json object and round share price to 2 decimal places
  try:
    #captures company name, stock ticker symbol, and currency of stock exchange
    name = response_dict_two["bestMatches"][0]['2. name']
    symbol_search = response_dict_two["bestMatches"][0]['1. symbol']
    currency = response_dict_two["bestMatches"][0]['8. currency']
  except:
    return('Please enter a valid ticker symbol')

  #Required data for GLOBAL QUOTE function, returns an object 'GLOBAL QUOTE' in csv,json,pandas
  data = {
      "function": "GLOBAL_QUOTE",
      "symbol": symbol_search,
      "outputsize": "compact",
      "datatype": "json",
      "apikey": apikey
      }

  #API call for GLOBAL QUOTE (MAX 5 requests per minute and 500 requests per day)
  response = requests.get(API_URL, params=data)

  #Create python dictionary with json data
  response_dict = json.loads(response.text)

  try:
    #captures stock price for given ticker symbol
    response_val = round(float(response_dict["Global Quote"]["05. price"]),2)
  except:
    return('Please enter a valid ticker symbol')
  
  return(name + ' ' + 'Current Price: $' + str(response_val) + ' ' + currency)



from cmc_api_key import api_key
from portfolio import symbols, symbol_list, BTC, ETH, XLM, XMR, ADA, ALGO, MGP, BTAH, PHX, AI, CMC_symbols
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
import pprint
import pandas as pd
import numpy as np
import plotly.express as px
import plotly
from datetime import date
#google api: from pytrends.request import TrendReq


#Call the API, the variable data is "returned"
url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'
parameters = {
  'symbol':CMC_symbols,
  'convert':'USD'
}
headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': api_key,
}
session = Session()
session.headers.update(headers)
try:
  response = session.get(url, params=parameters)
  data = json.loads(response.text)
  pprint.pprint(data) #<--------- all the DATA
except (ConnectionError, Timeout, TooManyRedirects) as e:
  print(e)

#=========================================================================================================================================================
#Find Portfolio USD Value
#USE A FUNCTION OR SOMETHING!!!!!!!!!!
#get_price function
def get_price(price_symbol):
  for d in data:
    price = data['data'][price_symbol]['quote']['USD']['price']
  return price

#Calculations To Find Portfolio Value
bitcoin_price =  get_price('BTC')
ethereum_price =  get_price('ETH')
lumen_price =  get_price('XLM')
monero_price =  get_price('XMR')
algorand_price = get_price('ALGO')
cardano_price = get_price('ADA')
bitcoin_value = BTC * bitcoin_price 
ethereum_value = ETH * ethereum_price 
lumen_value = XLM * lumen_price 
monero_value = XMR * monero_price 
cardano_value = ADA * cardano_price 
algorand_value = ALGO * algorand_price
#1 add here
# ,MGP,BTAH,PHX,AI
#
# 
#
MGP_value = MGP
BTAH_value = BTAH
PHX_value = PHX
AI_value = AI
portfolio_value = MGP_value + BTAH_value + PHX_value + AI_value + bitcoin_value + ethereum_value + lumen_value + monero_value + cardano_value + algorand_value
pprint.pprint('======================================================================================')

#Calculate and Print Percentages
bitcoin_percent = (100*bitcoin_value/portfolio_value)
ethereum_percent = (100*ethereum_value/portfolio_value) 
monero_percent = (100*monero_value/portfolio_value) 
lumen_percent = (100*lumen_value/portfolio_value) 
cardano_percent = (100*cardano_value/portfolio_value) 
algorand_percent = (100*algorand_value/portfolio_value)
#2 add here
# ,MGP,BTAH,PHX,AI
#
# 
#
MGP_percent = (100*MGP_value/portfolio_value)
BTAH_percent = (100*BTAH_value/portfolio_value)
PHX_percent = (100*PHX_value/portfolio_value)
AI_percent = (100*AI_value/portfolio_value)

#Calculations To Find BTC Value of each coin
bitcoin_BTC_value = BTC 
ethereum_BTC_value = ethereum_value / bitcoin_price
lumen_BTC_value = lumen_value / bitcoin_price
monero_BTC_value = monero_value / bitcoin_price
cardano_BTC_value = cardano_value / bitcoin_price
algorand_BTC_value = algorand_value / bitcoin_price
#3 add here
# ,MGP,BTAH,PHX,AI
#
# 
#
MGP_BTC_value = MGP_value / bitcoin_price
BTAH_BTC_value = BTAH_value / bitcoin_price
PHX_BTC_value = PHX_value / bitcoin_price
AI_BTC_value = AI_value / bitcoin_price

portfolio_BTC_value = MGP_BTC_value + BTAH_BTC_value + PHX_BTC_value + AI_BTC_value + bitcoin_BTC_value + ethereum_BTC_value + monero_BTC_value + lumen_BTC_value + cardano_BTC_value + algorand_BTC_value

#Print Percentages 
pprint.pprint('Percentages')
pprint.pprint('     BTC: '+ str(round(bitcoin_percent)) + '%')
pprint.pprint('     ETH: '+ str(round(ethereum_percent)) + '%')
pprint.pprint('     XMR: '+ str(round(monero_percent)) + '%')
pprint.pprint('     XLM: '+ str(round(lumen_percent)) + '%')
pprint.pprint('     ADA: '+ str(round(cardano_percent)) + '%')
pprint.pprint('     ALGO: '+ str(round(algorand_percent)) + '%')
#4 add here
# ,MGP,BTAH,PHX,AI
#
# 
#
pprint.pprint('     MGP: '+ str(round(MGP_percent)) + '%')
pprint.pprint('     BTAH: '+ str(round(BTAH_percent)) + '%')
pprint.pprint('     PHX: '+ str(round(PHX_percent)) + '%')
pprint.pprint('     AI: '+ str(round(AI_percent)) + '%')

pprint.pprint('======================================================================================')

#print Value in BTC
pprint.pprint('Value of Portfolio (BTC): '+ str(round(portfolio_BTC_value, 8)))
pprint.pprint('     BTC: '+ str(round(bitcoin_BTC_value, 3)))
pprint.pprint('     ETH: '+ str(round(ethereum_BTC_value, 3)))
pprint.pprint('     XMR: '+ str(round(monero_BTC_value, 3)))
pprint.pprint('     XLM: '+ str(round(lumen_BTC_value, 3)))
pprint.pprint('     ADA: '+ str(round(cardano_BTC_value, 3)))
pprint.pprint('     ALGO: '+ str(round(algorand_BTC_value, 3)))
#5 add here
# ,MGP,BTAH,PHX,AI
#
# 
#
pprint.pprint('     MGP: '+ str(round(MGP_BTC_value, 3)))
pprint.pprint('     BTAH: '+ str(round(BTAH_BTC_value, 3)))
pprint.pprint('     PHX: '+ str(round(PHX_BTC_value, 3)))
pprint.pprint('     AI: '+ str(round(AI_BTC_value, 3)))

pprint.pprint('======================================================================================')
#print Values in USD

pprint.pprint('Value of Portfolio (USD): ' + str(round(portfolio_value)))
pprint.pprint('     BTC: '+ str(round(bitcoin_BTC_value*bitcoin_price)))
pprint.pprint('     ETH: '+ str(round(ethereum_BTC_value*bitcoin_price)))
pprint.pprint('     XMR: '+ str(round(monero_BTC_value*bitcoin_price)))
pprint.pprint('     XLM: '+ str(round(lumen_BTC_value*bitcoin_price)))
pprint.pprint('     ADA: '+ str(round(cardano_BTC_value*bitcoin_price)))
pprint.pprint('     ALGO: '+ str(round(algorand_BTC_value*bitcoin_price)))
#6 add here
# ,MGP,BTAH,PHX,AI
#
# 
#
pprint.pprint('     MGP: '+ str(round(MGP_BTC_value*bitcoin_price)))
pprint.pprint('     BTAH: '+ str(round(BTAH_BTC_value*bitcoin_price)))
pprint.pprint('     PHX: '+ str(round(PHX_BTC_value*bitcoin_price)))
pprint.pprint('     AI: '+ str(round(AI_BTC_value*bitcoin_price)))

pprint.pprint('======================================================================================')


#=========================================================================================================================================================
#Starburst Szn
#step 1: create dataFrame
data_frame = {
        'Crypto':[portfolio_BTC_value,portfolio_BTC_value,portfolio_BTC_value,portfolio_BTC_value,portfolio_BTC_value,portfolio_BTC_value,portfolio_BTC_value,portfolio_BTC_value,portfolio_BTC_value,portfolio_BTC_value],
        'Name':['BTC', 'ETH', 'XLM', 'XMR', 'ADA', 'ALGO', 'MGP', 'BTAH', 'PHX', 'AI'],
        'Algorithm':['POW', 'POS', 'SCP', 'POW', 'POS', 'PPOS', 'VICs Masterpiece', 'VICs Masterpiece', 'Art', 'Art'],
        'Quantity':[BTC, ETH, XLM, XMR, ADA, ALGO, MGP, BTAH, PHX,AI],
        'USD Price':[bitcoin_price, ethereum_price, lumen_price, monero_price, cardano_price, algorand_price, MGP,BTAH,PHX,AI],
        'BTC Value':[bitcoin_BTC_value, ethereum_BTC_value, lumen_BTC_value, monero_BTC_value, cardano_BTC_value, algorand_BTC_value, MGP_BTC_value, BTAH_BTC_value, PHX_BTC_value, AI_BTC_value],
        'USD Value':[bitcoin_value, ethereum_value, lumen_value, monero_value, cardano_value, algorand_value, MGP_value,BTAH_value,PHX_value,AI_value],
        'Percent':[round(bitcoin_percent), round(ethereum_percent), round(lumen_percent), round(monero_percent), round(cardano_percent,2), round(algorand_percent,2), round(MGP_percent), round(BTAH_percent), round(PHX_percent), round(AI_percent)]}
#7 add here
# ,MGP,BTAH,PHX,AI
# USE TD Ameritrade API
# 
#
df = pd.DataFrame(data_frame)
print(df)

#step 2: export to excel
today = date.today()
print("Today's date:", today)
filename = 'frame_the_data' + str(today) + '.xlsx'
df.to_excel(filename)




df = pd.read_excel(filename, engine='openpyxl',)







#This sunburst isn't organized well!!!!!!!!!!!!!!!!!<------------------------
#can categorize based on POS,POW,PPOS
#or maybe percent_change_90d, cmc_rank, volume_24h, max_supply

#Percent Change Analysis w/ Sunburst
#Step 1: Declare And Assign 6 Percent Change Variables for each Asset 
# 
# <UNUSED>!!!!!!!!

#INDEX NEEDS TO BE AUTOMATIC (for more symbols 10k+)!!!! <----------------------------------------------------------------------

#pprint.pprint(new_percents)

#Step 3: Make another Sunburst with percents
#read the data from frame_the_data file  and the new_percents file
df_portfolio = pd.read_excel('frame_the_data.xlsx', engine='openpyxl',)



# </UNUSED!!!>

#how to get the number value?????
#reorganize dataframe with symbol as the index
#get rid of index value
#finish sunburst

#=========================================================================================================================================================

#TD Ameritrade API part

#more colors

#Use twitter API to track Founders

print('bye')
#print("A MOLNAR & NISBETT CONSULTING PROGRAM")


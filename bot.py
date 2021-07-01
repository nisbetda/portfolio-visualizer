from cmc_api_key import api_key
from portfolio import symbols, symbol_list, BTC, ETH, XLM, XMR, ADA, ALGO
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


#=========================================================================================================================================================

#=================== C R Y P T O _ C U S T O M S - PORTFOLIO TRACKER =====================================================================================

#=========================================================================================================================================================

#Call the API, the variable data is "returned"
url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'
parameters = {
  'symbol':symbols,
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
portfolio_value = bitcoin_value + ethereum_value + lumen_value + monero_value + cardano_value + algorand_value
pprint.pprint('=========================================================================================================================================================')
pprint.pprint('USD Value of Portfolio: ' + str(portfolio_value))

#Print Percentages
pprint.pprint('     bitcoin: '+ str(100*bitcoin_value/portfolio_value) + '%')
pprint.pprint('     ethereum: '+ str(100*ethereum_value/portfolio_value) + '%')
pprint.pprint('     monero: '+ str(100*monero_value/portfolio_value) + '%')
pprint.pprint('     lumen: '+ str(100*lumen_value/portfolio_value) + '%')
pprint.pprint('     cardano: '+ str(100*cardano_value/portfolio_value) + '%')
pprint.pprint('     algorand: '+ str(100*algorand_value/portfolio_value) + '%')

#Calculations To Find Portfolio BTC Value
bitcoin_BTC_value = BTC 
ethereum_BTC_value = ethereum_value / bitcoin_price
lumen_BTC_value = lumen_value / bitcoin_price
monero_BTC_value = monero_value / bitcoin_price
cardano_BTC_value = cardano_value / bitcoin_price
algorand_BTC_value = algorand_value / bitcoin_price
portfolio_BTC_value = bitcoin_BTC_value + ethereum_BTC_value + monero_BTC_value + lumen_BTC_value + cardano_BTC_value + algorand_BTC_value

#print BTC Values
pprint.pprint('BTC Value of Portfolio: '+ str(portfolio_BTC_value))
pprint.pprint('     bitcoin: '+ str(bitcoin_BTC_value))
pprint.pprint('     ethereum: '+ str(ethereum_BTC_value))
pprint.pprint('     monero: '+ str(monero_BTC_value))
pprint.pprint('     lumen: '+ str(lumen_BTC_value))
pprint.pprint('     cardano: '+ str(cardano_BTC_value))
pprint.pprint('     algorand: '+ str(algorand_BTC_value))

pprint.pprint('=========================================================================================================================================================')
#=========================================================================================================================================================
#Starburst Szn
#step 1: create dataFrame
data_frame = {'Name':['BTC', 'ETH', 'XLM', 'XMR', 'ADA', 'ALGO'],
        'Quantity':[BTC, ETH, XLM, XMR, ADA, ALGO],
        'USD Price':[bitcoin_price, ethereum_price, lumen_price, monero_price, cardano_price, algorand_price],
        'BTC Value':[bitcoin_BTC_value, ethereum_BTC_value, lumen_BTC_value, monero_BTC_value, cardano_BTC_value, algorand_BTC_value],
        'USD Value':[bitcoin_value, ethereum_value, lumen_value, monero_value, cardano_value, algorand_value]}

df = pd.DataFrame(data_frame)
print(df)

#step 2: export to excel
today = date.today()
print("Today's date:", today)
filename = 'frame_the_data' + str(today) + '.xlsx'
df.to_excel(filename)

#step 3: starburst from excel file (very unnecessary)
#read the data from frame_the_data file 
df = pd.read_excel(filename, engine='openpyxl',)
#print(df)
Name = df['Name']
Quantity = df['Quantity']
USD_Price = df['USD Price']
USD_Value = df['USD Value']
BTC_Value = df['BTC Value']

#the visualization party 
fig = px.sunburst(df,
                 path = [Name, Quantity],
                 values = BTC_Value,
                 color = BTC_Value,
                 color_continuous_scale = ['gold', 'green'],
                 title = 'Crypto Portfolio'
                 )

plotly.offline.plot(fig, filename = 'Crypto_Sunburst.html')

#This sunburst isn't organized well!!!!!!!!!!!!!!!!!<------------------------
#can categorize based on POS,POW,PPOS
#or maybe percent_change_90d, cmc_rank, volume_24h, max_supply

#Percent Change Analysis w/ Sunburst
#Step 1: Declare And Assign 6 Percent Change Variables for each Asset
def get_percent_change(quote_symbol):
  percent_change_list = []
  num_of_symbols = 0
  for s in symbol_list:
      num_of_symbols += 1
      percent_change_1h = data['data'][s]['quote']['USD']['percent_change_1h']
      percent_change_24h = data['data'][s]['quote']['USD']['percent_change_24h']
      percent_change_7d = data['data'][s]['quote']['USD']['percent_change_7d']
      percent_change_30d = data['data'][s]['quote']['USD']['percent_change_30d']
      percent_change_60d = data['data'][s]['quote']['USD']['percent_change_60d']
      percent_change_90d = data['data'][s]['quote']['USD']['percent_change_90d']

      percent_change_list.append(percent_change_1h)
      percent_change_list.append(percent_change_24h)
      percent_change_list.append(percent_change_7d)
      percent_change_list.append(percent_change_30d)
      percent_change_list.append(percent_change_60d)
      percent_change_list.append(percent_change_90d)

  df_percent = pd.DataFrame(percent_change_list)

  return df_percent, num_of_symbols

#Step 2: Create Data Frame for variables
percents, num_of_symbols =  get_percent_change(symbol_list)
#change dimensions
new_percents = percents.values.copy()
#converted to a numpy array, why? idk.
new_percents.resize((len(symbol_list)), 6) #find a way to find length of list of symbols
pd.DataFrame(new_percents.T)
# convert array into a dataframe
df_from_np = pd.DataFrame(new_percents.T)
# save to xlsx file
df_from_np.to_excel('new_percents.xlsx', index = ['BTC', 'ETH', 'XLM', 'XMR', 'ALGO', 'ADA'], header = ['percent_change_1h', 'percent_change_24h', 'percent_change_7d', 'percent_change_30d', 'percent_change_60d', 'percent_change_90d'])

#INDEX NEEDS TO BE AUTOMATIC (for more symbols 10k+)!!!! <----------------------------------------------------------------------

#pprint.pprint(new_percents)

#Step 3: Make another Sunburst with percents
#read the data from frame_the_data file  and the new_percents file
df_portfolio = pd.read_excel('frame_the_data.xlsx', engine='openpyxl',)
df_percent = pd.read_excel('new_percents.xlsx', engine='openpyxl',)

Name = df_portfolio['Name']
Quantity = df_portfolio['Quantity']
USD_Price = df_portfolio['USD Price']
USD_Value = df_portfolio['USD Value']
BTC_Value = df_portfolio['BTC Value']

percent_change_1h = df_percent['percent_change_1h']
percent_change_24h = df_percent['percent_change_24h']
percent_change_7d = df_percent['percent_change_7d']
percent_change_30d = df_percent['percent_change_30d']
percent_change_60d = df_percent['percent_change_60d']
percent_change_90d = df_percent['percent_change_90d']

percent_name_list = ['percent_change_1h', 'percent_change_24h', 'percent_change_7d', 'percent_change_30d', 'percent_change_60d', 'percent_change_90d']
percent_value_list = [percent_change_1h, percent_change_24h, percent_change_7d, percent_change_30d, percent_change_60d, percent_change_90d]

#find the number of positive percentage changes for each symbol
#split dataframe by row
df_percent_1 = df_percent.iloc[0,:]
df_percent_2 = df_percent.iloc[1,:]
df_percent_3 = df_percent.iloc[2,:]
df_percent_4 = df_percent.iloc[3,:]
df_percent_5 = df_percent.iloc[4,:]
df_percent_6 = df_percent.iloc[5,:]

hour_1 = df_percent_1.iloc[[0,1]]
hour_24 = df_percent_1.iloc[[0,2]]
day_7 = df_percent_1.iloc[[0,3]]
day_30 = df_percent_1.iloc[[0,4]]
day_60 = df_percent_1.iloc[[0,5]]
day_90 = df_percent_1.iloc[[0,6]]
#Why Are These Values Not Regular Ints?????? <----------
#print(percent_change_1h.take[[0,0]])
 
#how to get the number value?????
#reorganize dataframe with symbol as the index
#get rid of index value
#finish sunburst
#def get_percent_change(quote_symbol):
  #for s in symbol_list:
#the visualization party pt. 2
fig = px.sunburst(
                 path = [Name],
                 #color = percent_value_list,
                 color_continuous_scale = ['red', 'green'],
                 title = 'Crypto Percents'
                 )
#plotly.offline.plot(fig, filename = 'Crypto_Percent_Sunburst.html')
#Step 4: Profit??????
#=========================================================================================================================================================

#use Kraken's API to place buy and sell orders based on R&A

#more colors

#Use twitter API to track Founders


print("bye")

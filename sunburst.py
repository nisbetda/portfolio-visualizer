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
#=========================================================================================================================================================
#Make a sunburst without calling the API (don't have unlimited calls)
#read the data from frame_the_data file 
df = pd.read_excel('new_percents.xlsx', engine='openpyxl')
print(df)
percent_change_1h = df['percent_change_1h']
percent_change_24h = df['percent_change_24h']
percent_change_7d = df['percent_change_7d']
percent_change_30d = df['percent_change_30d']
percent_change_60d = df['percent_change_60d']
percent_change_90d = df['percent_change_90d']

fig = px.sunburst(df,
                 path = [ symbol_list, percent_change_90d],
                 hover_name = symbol_list,
                 color_discrete_map={'BTC':'gold', 'ETH':'silver', 'XLM':'gold', 'XMR':'silver','ADA':'gold', 'ALGO':'black',},
                 color = percent_change_90d,
                 #color_continuous_scale = ['red', 'green'],
                 title = 'Crypto Percents'
                 )

#plotly.offline.plot(fig, filename = 'External_Sunburst.html')

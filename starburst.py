#=============================Molnar & Nisbett Consulting=====================================================================================

#=================================PORTFOLIO TRACKER=====================================================================================

#=================================================================================================================================================================================================
from calculations import filename, pd, today, df
import plotly.express as px
import plotly
from datetime import date
#================================================================================================================================================================================================
#Creates a Starburst Chart
Crypto, Name, Algorithm, Quantity, USD_Price, USD_Value, BTC_Value, Percent = df['Crypto'], df['Name'], df['Algorithm'], df['Quantity'], df['USD Price'], df['USD Value'], df['BTC Value'], df['Percent']

#the visualization party 
fig = px.sunburst(df,path = [Crypto, Name, Percent], values = Percent, title = 'Portfolio')
fig.show()

#save to file called "Crypto_Sunburst(today's date)"
plotly.offline.plot(fig, filename = 'Crypto_Sunburst' + str(today) + '.html')
#================================================================================================================================================================================================

#==To Do:

#==Use Kraken's API to place buy and sell orders based on R&A

#==Use twitter API to track Founders

#==More colors!!!!!!!!!!!!!!!!!!!!!!

#==add this to sunburst graph
#percent_change_1h = df['percent_change_1h']
#percent_change_24h = df['percent_change_24h']
#percent_change_7d = df['percent_change_7d']
#percent_change_30d = df['percent_change_30d']
#percent_change_60d = df['percent_change_60d']
#percent_change_90d = df['percent_change_90d']
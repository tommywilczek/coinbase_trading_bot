from coinbase.wallet.client import Client
from time import sleep
from datetime import datetime
from data import api_key, api_secret

#https://developers.coinbase.com/docs/wallet/guides/buy-sell

#Setting up coinbase client
client = Client(api_key, api_secret)

buy_price = float(client.get_buy_price(currency_pair = 'ADA-USD').amount)
print("Buy price:", buy_price)

sell_price = float(client.get_sell_price(currency_pair = 'ADA-USD').amount)
print("Sell price:", sell_price)        


usd_wallet = 100

ada_wallet = 0

times_bought = 0

times_sold = 0

print("BUYING ONE ADA")
usd_wallet -= buy_price
ada_wallet += 1
times_bought += 1
prev_buy_price = buy_price

while (True):
    print("=====================================================")
    print("=====================================================")
    full_time_now = datetime.now()
    print("Time:", full_time_now.hour, ":", full_time_now.minute)

    print("USD Wallet balance: $", usd_wallet)
    print("ADA Wallet balance:", ada_wallet)

    buy_price = float(client.get_buy_price(currency_pair = 'ADA-USD').amount)
    print("Buy price:", buy_price)

    sell_price = float(client.get_sell_price(currency_pair = 'ADA-USD').amount)
    print("Sell price:", sell_price)

    print("Total USD spent:", sell_price)

    if((buy_price < prev_buy_price) and usd_wallet > 0):
        print("BUYING ONE ADA")
        usd_wallet -= buy_price
        ada_wallet += 1
        times_bought += 1
        prev_buy_price = buy_price

    if((sell_price > prev_buy_price) and ada_wallet > 0):
        print("SELLING ALL ADA")
        money_earned = ada_wallet * sell_price
        usd_wallet += money_earned
        ada_wallet = 0
        times_sold += 1



    sleep(1800)
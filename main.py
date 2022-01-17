import requests
import os
id = 0
usdbal = '10'
usdbalm = float(usdbal)
usdbal = float(usdbal)
opened = {}
musdbal = usdbal
musdbal = float(usdbal)
clear = lambda: os.system('clear')

def get_price(symbol, prices):
    for price in prices:
        if symbol == price['symbol']:
            return price['price']


while True:
    if usdbal < 0:
        usdbal = 0
    usdbal = round(usdbal, 2)
    print('balance:', usdbal, '$')
    print('opened deals:')
    if opened == {}:
        print('None')
    for key in opened.keys():
        print(key, '->', opened[key])

    for ch in opened.keys():
        openprice = opened[ch][0]
        symbol = opened[ch][1]
        leverage = opened[ch][2]
        amount = opened[ch][3]
        direction = opened[ch][4]

        if direction == 'short':
            prices = requests.get('https://api.binance.com/api/v3/ticker/price').json()
            curprice = get_price(symbol, prices)
            curprice = float(curprice)
            openprice = float(openprice)
            leverage = float(leverage)
            profit = curprice / openprice * 100 - 100
            profit = profit * leverage
            profit = profit / 100
            profit = profit * -1
            musdbal = amount * profit + amount + usdbal
            musdbal = round(musdbal, 2)
            print('≈', musdbal, '$')
        else:
            prices = requests.get('https://api.binance.com/api/v3/ticker/price').json()
            curprice = get_price(symbol, prices)

            curprice = float(curprice)
            openprice = float(openprice)
            leverage = float(leverage)
            profit = curprice / openprice * 100 - 100
            profit = profit * leverage
            profit = profit / 100
            musdbal = amount * profit + amount + usdbal
            musdbal = round(musdbal, 2)
            print('≈', musdbal, '$')

    id = id + 1
    ch1 = input('1-open, 2-close: ')
    if ch1 == '1':
        ch = input('1-short, 2-long : ')
        if ch == '1':
            try:
                symbol = input('crypto: ')
                symbol = symbol.upper() + 'USDT'
                leverage = input('leverage: ')
                leverage = float(leverage)
                if leverage > 0 and leverage <= 120:
                    leverage = float(leverage)
                    amount = input('amount: ')
                    amount = float(amount)
                    if amount <= usdbal:
                        prices = requests.get('https://api.binance.com/api/v3/ticker/price').json()
                        price = get_price(symbol, prices)
                        price = float(price)
                        dict = {}
                        usdbal = usdbal - amount
                        direction = 'short'
                        dict[id] = price, symbol, leverage, amount, direction
                        opened.update(dict)
            except:
                print('Error. Try again.')
        if ch == '2':
            try:
                symbol = input('crypto: ')
                symbol = symbol.upper() + 'USDT'
                leverage = input('leverage: ')
                leverage = float(leverage)
                if leverage > 0 and leverage <= 120:
                    leverage = float(leverage)
                    amount = input('amount: ')
                    amount = float(amount)
                    if amount <= usdbal:
                        prices = requests.get('https://api.binance.com/api/v3/ticker/price').json()
                        price = get_price(symbol, prices)
                        price = float(price)
                        dict = {}
                        usdbal = usdbal - amount
                        direction = 'long'
                        dict[id] = price, symbol, leverage, amount, direction
                        opened.update(dict)
            except:
                print('Error. Try again.')
    if ch1 == '2':
        try:
            print(opened)
            ch = input('id: ')
            ch = int(ch)
            openprice = opened[ch][0]
            symbol = opened[ch][1]
            leverage = opened[ch][2]
            amount = opened[ch][3]
            direction = opened[ch][4]

            if direction == 'short':
                prices = requests.get('https://api.binance.com/api/v3/ticker/price').json()
                curprice = get_price(symbol, prices)
                curprice = float(curprice)
                openprice = float(openprice)
                leverage = float(leverage)
                profit = curprice / openprice * 100 - 100
                profit = profit * leverage
                profit = profit / 100
                profit = profit * -1
                usdbal = amount * profit + amount + usdbal
                print(usdbal)
                opened.pop(ch)
                id = 0
            else:
                prices = requests.get('https://api.binance.com/api/v3/ticker/price').json()
                curprice = get_price(symbol, prices)

                curprice = float(curprice)
                openprice = float(openprice)
                leverage = float(leverage)
                profit = curprice / openprice * 100 - 100
                profit = profit * leverage
                profit = profit / 100
                usdbal = amount * profit + amount + usdbal
                print(usdbal)
                opened.pop(ch)
                id = 0
        except:
            print('Error. Try again.')
    clear()
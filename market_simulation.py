import random

from datetime import datetime, timedelta


from src.stock import StockType, Stock
from src.trade import TradeIndicator, Trade
from src.calculate import gbce, pe_ratio, volume_weighted_stock_price, \
        dividend_yield


def get_quantity():
    return random.randint(0, 10000)


def get_timestamp():
    interval = random.randint(0, 30)
    return datetime.now() - timedelta(minutes=interval)


def get_indicator():
    return random.choice([TradeIndicator.BUY.value, TradeIndicator.SELL.value])


def get_stock_type():
    return random.choice([StockType.COMMON.value, StockType.PREFERRED.value])


def get_trade_price():
    return random.randint(1, 100)


def get_market_price():
    return random.randint(1, 10)


TEST_DATA = [
    {"symbol": "TEA", "stock_type": get_stock_type(),
     "last_dividend": 0, "fixed_dividend": 0, "par_value":100,
     "market_price": get_market_price(),
     "trade": {
         "quantity": get_quantity(),
         "timestamp": get_timestamp(),
         "indicator": get_indicator(),
         "price": get_trade_price()
     }},
    {"symbol": "POP", "stock_type": get_stock_type(),
     "last_dividend": 8, "fixed_dividend": 0, "par_value": 100,
     "market_price": get_market_price(),
     "trade": {
         "quantity": get_quantity(),
         "timestamp": get_timestamp(),
         "indicator": get_indicator(),
         "price": get_trade_price()
     }},
    {"symbol": "ALE", "stock_type": get_stock_type(),
     "last_dividend": 23, "fixed_dividend": 0, "par_value": 60,
     "market_price": get_market_price(),
     "trade": {
         "quantity": get_quantity(),
         "timestamp": get_timestamp(),
         "indicator": get_indicator(),
         "price": get_trade_price()
     }},
    {"symbol": "GIN", "stock_type": get_stock_type(),
     "last_dividend": 8, "fixed_dividend": 2, "par_value": 100,
     "market_price": get_market_price(),
     "trade": {
         "quantity": get_quantity(),
         "timestamp": get_timestamp(),
         "indicator": get_indicator(),
         "price": get_trade_price()
     }},
    {"symbol": "JOE", "stock_type": get_stock_type(),
     "last_dividend": 13, "fixed_dividend": 0, "par_value": 250,
     "market_price": get_market_price(),
     "trade": {
         "quantity": get_quantity(),
         "timestamp": get_timestamp(),
         "indicator": get_indicator(),
         "price": get_trade_price()
     }}
]


def simulate_market():
    all_trades = []
    for item in TEST_DATA:
        current_trade_raw = item.pop('trade')
        current_stock = Stock(**item)
        current_trade_raw['stock'] = current_stock
        current_trade = Trade(**current_trade_raw)
        all_trades.append(current_trade)
    return all_trades


def get_last_fifteen_minutes_trades(trades):
    now = datetime.now()
    fifteen_mins_ago = now - timedelta(minutes=15)
    return [trade for trade in trades
            if trade.timestamp > fifteen_mins_ago]


market = simulate_market()
recent = get_last_fifteen_minutes_trades(market)

print("Current market:\n")
for trade in market:
    fmt = "{} | Dividend yield: {} | P/E Ratio: {}\n"
    print(fmt.format(trade, dividend_yield(trade.stock), pe_ratio(trade.stock)))

print("GBCE index: {}".format(gbce([trade.stock for trade in market])))
print("Volume weighted stock price: {}".format(volume_weighted_stock_price(recent)))

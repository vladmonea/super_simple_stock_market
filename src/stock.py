from enum import Enum


class StockType(Enum):
    COMMON = "Common"
    PREFERRED = "Preferred"


class Stock(object):

    def __init__(self, symbol, stock_type, last_dividend, fixed_dividend,
                 par_value, market_price):
        self.symbol = symbol
        self.stock_type = stock_type
        self.last_dividend = last_dividend
        self.fixed_dividend = fixed_dividend
        self.par_value = par_value
        self.market_price = market_price

    def __repr__(self):
        fmt = "Stock: {} | Type: {} | Last Dividend: {} | Fixed Dividend: {} | Par Value : {} | Market price: {}\n"
        return fmt.format(self.symbol, self.stock_type, self.last_dividend,
                         self.fixed_dividend, self.par_value, self.market_price)


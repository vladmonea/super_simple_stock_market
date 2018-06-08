from enum import Enum
from datetime import datetime

from .stock import Stock


class TradeIndicator(Enum):
    BUY = "Buy"
    SELL = "Sell"


class Trade(object):

    def __init__(self, stock, timestamp, quantity, indicator, price):
        self.stock = stock
        self.timestamp = timestamp if timestamp else None
        self.quantity = quantity
        self.indicator = indicator
        self.price = price

    def __repr__(self):
        fmt = "Trade summary\nStock: {} | Time: {} | Trade Indicator: {} | Quantity: {} | Price: {}\n"
        return fmt.format(self.stock.symbol, self.timestamp,
                         self.indicator, self.quantity, self.price)

    @property
    def stock(self):
        return self._stock

    @stock.setter
    def stock(self, value):
        if not type(value) == Stock:
            raise TypeError("Expected value of type Stock.")
        self._stock = value

    @property
    def timestamp(self):
        return self._timestamp

    @timestamp.setter
    def timestamp(self, value):
        if value is None:
            value = datetime.now()
        self._timestamp = value

    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, value):
        self._quantity = value

    @property
    def trade_type(self):
        return self._trade_type

    @trade_type.setter
    def trade_type(self, value):
        if not type(value) == TradeType:
            raise ValueError("Expected TradeType object.")
        self._trade_type = value


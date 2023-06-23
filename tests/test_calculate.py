from src.calculate import gbce, dividend_yield, pe_ratio, volume_weighted_stock_price
from src.stock import Stock, StockType


def test_pe_ratio(get_indicator, get_market_price, get_timestamp):
    test_stock_data = {"symbol": "TEA", "stock_type": get_stock_type(),
        "last_dividend": 2, "fixed_dividend": 0, "par_value":100,
        "market_price": 10,
        "trade": {
            "quantity": 100,
            "timestamp": get_timestamp(100),
            "indicator": get_indicator("BUY"),
            "price": 50
        }
     }
     test_stock = Stock(**test_stock_data)
     per = pe_ratio(test_stock)

     assert per == 5

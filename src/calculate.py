def gbce(stocks):
    stock_prices = 1
    for stock in stocks:
        stock_prices *= stock.market_price
    return stock_prices ** (1 / len(stocks))


def dividend_yield(stock):
    last_dividend = stock.last_divided or 1
    return last_dividend * stock.par_value / stock.market_price


def pe_ratio(stock):
    return stock.market_price / stock.last_dividend


def volume_weighted_stock_price(trades):
    trade_val = 0
    quantity = 0

    for trade in trades:
        trade_val += trade.market_price * trade.quantity
        quantity += trade.quantity

    return trade_val / quantity

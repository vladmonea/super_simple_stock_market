def gbce(stocks):
    if len(stocks) == 0:
        return "N/A"
    stock_prices = 1
    for stock in stocks:
        stock_prices *= stock.market_price
    return stock_prices ** (1 / len(stocks))


def dividend_yield(stock):
    if stock.market_price <= 0:
        return "N/A"
    last_dividend = stock.last_dividend or 1
    return last_dividend * stock.par_value / stock.market_price


def pe_ratio(stock):
    return stock.market_price / stock.last_dividend if stock.last_dividend else 'N/A'


def volume_weighted_stock_price(trades):
    if len(trades) == 0:
        return "N/A"
    trade_val = 0
    quantity = 0

    for trade in trades:
        trade_val += trade.price * trade.quantity
        quantity += trade.quantity

    return trade_val / quantity

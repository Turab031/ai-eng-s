import yfinance as yf
import json

def get_stock_price(ticker_symbol:str)->str:
    """fetch the current price of a stock given it's ticker symbol"""
    try:
        stock=yf.Ticker(ticker_symbol.upper())
        price=stock.fast_info['last_price']
        currency = stock.fast_info["currency"]
        return json.dumps({
            "ticker":ticker_symbol.upper(),
            "price":price,
            "currency":currency
        })
    except Exception as e:
        print(f"error fetching stock price for {ticker_symbol}:{e}")
        return json.dumps({"error":str(e)})
    
    
if __name__=="__main__":
    print(get_stock_price("TSLA"))
    
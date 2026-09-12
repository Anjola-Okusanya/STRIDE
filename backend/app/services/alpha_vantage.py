import requests
import os

def get_live_price(ticker: str) -> float:
    if ticker == "CASH":
        return 1.0
    
    api_key = os.getenv("ALPHA_VANTAGE_KEY")
    url = (
        f"https://www.alphavantage.co/query"
        f"?function=GLOBAL_QUOTE"
        f"&symbol={ticker}"
        f"&apikey={api_key}"
    )
    
    response = requests.get(url)
    data = response.json()
    
    price = data["Global Quote"]["05. price"]
    return float(price)
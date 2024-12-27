import requests
import pyttsx3

def get_bitcoin_price():
    """Fetches the current price of Bitcoin in USD using CoinGecko API."""
    url = "https://api.coingecko.com/api/v3/simple/price"
    params = {
        "ids": "bitcoin",
        "vs_currencies": "usd"
    }
    
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()  # Raise an HTTPError for bad responses (4xx and 5xx)
        data = response.json()
        bitcoin_price = data["bitcoin"]["usd"]
        print(f"Current Bitcoin Price: ${bitcoin_price}")
        return bitcoin_price
    except requests.exceptions.RequestException as e:
        print(f"Error fetching Bitcoin price: {e}")
        return None



def announce_bitcoin_price(price):
    """Announces the Bitcoin price using text-to-speech."""
    engine = pyttsx3.init()
    engine.say(f"The current price of Bitcoin is {price} dollars.")
    engine.runAndWait()

if __name__ == "__main__":
    price = get_bitcoin_price()
    if price:
        announce_bitcoin_price(price)


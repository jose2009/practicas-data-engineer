import requests

BASE_URL = "https://api.coingecko.com/api/v3/coins"

def extract_data(crypto, days = 30):
    url = f"{BASE_URL}/{crypto}/market_chart"
    params = { "vs_currency": "usd",
                "days": days}
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print (f"error al obtener datos de {crypto}: {e}")
        return None
        
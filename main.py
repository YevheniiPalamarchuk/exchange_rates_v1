import requests

API_KEY = "" # I keep my api key safe via proxy
url = f"https://api.freecurrencyapi.com/v1/latest?apikey={API_KEY}&base_currency=USD&currencies=EUR,GBP,PLN,JPY"

response = requests.get(url)
data = response.json()

for currency, rate in data["data"].items():
    print(f"1 USD = {rate} {currency}")

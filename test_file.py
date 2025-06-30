from flask import Flask, request, jsonify
import requests
import os

app = Flask(__name__)

API_KEY = os.getenv("CURRENCY_API_KEY")

@app.route('/exchange', methods=['GET'])
def get_exchange_rates():
    base = request.args.get("base", "USD")
    currencies = request.args.get("currencies", "EUR,GBP,PLN,JPY,RUB,UAH")

    if not API_KEY:
        return jsonify({"error": "API key not set"}), 500

    url = f"https://api.freecurrencyapi.com/v1/latest?apikey={API_KEY}&base_currency={base}&currencies={currencies}"
    response = requests.get(url)

    if response.status_code != 200:
        return jsonify({"error": "Failed to fetch data"}), response.status_code

    return jsonify(response.json())

if __name__ == "__main__":
    app.run(debug=True)

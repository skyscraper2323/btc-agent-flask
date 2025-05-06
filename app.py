from flask import Flask, jsonify
import requests
import datetime

app = Flask(__name__)

@app.route("/")
def home():
    return "BTC Agent działa ✅"

@app.route("/btc", methods=["GET"])
def get_btc_price():
    try:
        now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        response = requests.get("https://api.coingecko.com/api/v3/simple/price", params={
            "ids": "bitcoin",
            "vs_currencies": "usd"
        })
        data = response.json()
        price = data.get("bitcoin", {}).get("usd")
        if price is None:
            raise ValueError("Brak ceny w odpowiedzi z API")
        return jsonify({"timestamp": now, "btc_usd": price})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

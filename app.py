from flask import Flask, jsonify
import requests
import datetime
import os

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

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)

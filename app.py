from flask import Flask, request, jsonify
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
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice/BTC.json")
        price = round(response.json()["bpi"]["USD"]["rate_float"], 2)
        return jsonify({"timestamp": now, "btc_usd": price})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

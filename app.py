import gradio as gr
import datetime
import requests

def btc_agent(query):
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    price = get_btc_price()
    if "kurs" in query.lower() or "cena" in query.lower():
        return f"🕒 {now}\n💰 Aktualny kurs BTC to {price} USD"
    return "Nie rozumiem pytania. Zapytaj np. o kurs BTC."

def get_btc_price():
    try:
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice/BTC.json")
        return round(response.json()["bpi"]["USD"]["rate_float"], 2)
    except Exception as e:
        return f"Błąd: {e}"

iface = gr.Interface(fn=btc_agent, inputs="text", outputs="text", title="Agent BTC")
iface.launch()
import requests
from flask import Flask, jsonify
import os
from threading import Lock

from backend.memory_cache import get_cached
from backend.coingeko_call import fetch_crypto_prices

app = Flask(__name__)
PORT = int(os.getenv("PORT", "8080"))

COINGECKO_URL = (
    "https://api.coingecko.com/api/v3/simple/price"
    "?ids=bitcoin,ethereum&vs_currencies=usd&include_24hr_change=true"
)

@app.route("/market-summary")
def market_summary():
    payload = get_cached("market-summary", fetch_crypto_prices)
    return jsonify(payload)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=PORT)
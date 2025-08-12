# salesforce-api-dashboard

This project provides a simple API to fetch and serve cryptocurrency price data (Bitcoin and Ethereum) using Flask, with in-memory caching and data from the CoinGecko API.

## Project Structure
- `app.py`: Main Flask application exposing the API endpoint.
- `backend/coingeko_call.py`: Fetches crypto prices from CoinGecko and formats the response.
- `backend/memory_cache.py`: Simple in-memory cache to reduce API calls.

## How It Works

### 1. API Endpoint
- The Flask app exposes `/market-summary`.
- When this endpoint is called, it returns a JSON summary of the latest Bitcoin and Ethereum prices, their 24h change, and the last update timestamp.

### 2. Caching
- The `get_cached` function in `memory_cache.py` caches the API response for 60 seconds (configurable).
- If a cached value exists and is fresh, it is returned immediately. Otherwise, a new API call is made.

### 3. Fetching Prices
- `fetch_crypto_prices` in `coingeko_call.py` calls the CoinGecko API for Bitcoin and Ethereum prices in USD.
- The response is formatted as:

```json
{
  "updatedAt": 1723372800,
  "assets": [
    {"symbol": "BTC", "priceUsd": 12345.67, "change24h": 1.23},
    {"symbol": "ETH", "priceUsd": 2345.67, "change24h": -0.56}
  ]
}
```

### 4. Error Handling
- Network, timeout, and JSON errors are handled gracefully and return an error message in the response.

## How to Run
1. Install dependencies: `pip install flask requests`
2. Run the app: `python app.py`
3. Access the API at: `http://localhost:8080/market-summary`

## Customization
- To add more coins, update the `coins` and `key_map` in `fetch_crypto_prices`.
- Adjust cache TTL in `memory_cache.py` as needed.
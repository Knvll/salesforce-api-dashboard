# This script fetches the current prices of Bitcoin and Ethereum in USD from the CoinGecko API.
import requests
import logging
from typing import Dict, Any, List
import time

def fetch_crypto_prices(
    coins: List[str] = ["bitcoin", "ethereum"],
    vs_currency: str = "usd",
    timeout: float = 5,
    key_map: Dict[str, str] = {"bitcoin": "BTC", "ethereum": "ETH"}
) -> Dict[str, Any]:
    """
    Fetch current prices and 24hr change for given cryptocurrencies from CoinGecko API.
    Args:
        coins: List of coin IDs to fetch (default: ["bitcoin", "ethereum"])
        vs_currency: The fiat currency to compare against (default: "usd")
        timeout: Timeout for the API request in seconds (default: 0.5)
        key_map: Mapping from CoinGecko IDs to desired output keys
    Returns:
        Dictionary with coin data or error message.
    """
    url = (
        f"https://api.coingecko.com/api/v3/simple/price?ids={','.join(coins)}"
        f"&vs_currencies={vs_currency}&include_24hr_change=true"
    )
    logging.info(f"Fetching crypto prices from {url}")
    try:
        response = requests.get(url, timeout=timeout)
        response.raise_for_status()
        try:
            data = response.json()
            # Remap keys using key_map
            remapped = {
            "updatedAt": int(time.time()),
            "assets": [
                {
                    "symbol": "BTC",
                    "priceUsd": data["bitcoin"]["usd"],
                    "change24h": data["bitcoin"].get("usd_24h_change"),
                },
                {
                    "symbol": "ETH",
                    "priceUsd": data["ethereum"]["usd"],
                    "change24h": data["ethereum"].get("usd_24h_change"),
                },
            ],
        }
            return remapped
        except ValueError:
            logging.error("Error parsing JSON response.")
            return {"error": "Invalid JSON response from API."}
    except requests.exceptions.Timeout:
        logging.error("Request timed out. Please try again later.")
        return {"error": "Request timed out."}
    except requests.exceptions.RequestException as e:
        logging.error(f"Network error: {e}")
        return {"error": f"Network error: {e}"}

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    result = fetch_crypto_prices()
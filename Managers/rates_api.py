import datetime

import requests

base_url :str = "https://tassidicambio.bancaditalia.it/terzevalute-wf-web/rest/v1.0"
header = {"Accept": "application/json"}

def get_daily(d :datetime):
    request = f"{base_url}/dailyRates?" \
              f"referenceDate={d:%Y-%m-%d}" \
              f"&baseCurrencyIsoCode=USD" \
              f"&baseCurrencyIsoCode=JPY" \
              f"&baseCurrencyIsoCode=AUD" \
              f"&baseCurrencyIsoCode=RUB" \
              f"&currencyIsoCode=EUR" \
              f"&lang=en"

    response = requests.get(request, headers=header)
    return response.json()
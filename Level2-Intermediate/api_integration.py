import requests

url = "https://open.er-api.com/v6/latest/USD"

try:
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()

        eur = data["rates"]["EUR"]
        gbp = data["rates"]["GBP"]
        inr = data["rates"]["INR"]

        print("=== Currency Exchange Rates (Base: USD) ===")
        print("EUR:", eur)
        print("GBP:", gbp)
        print("INR:", inr)

    else:
        print("Error: Failed to fetch data. Status code:", response.status_code)

except Exception as e:
    print("An error occurred:", e)
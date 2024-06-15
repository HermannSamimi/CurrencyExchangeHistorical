import requests
import datetime


def main():   
    base_currency = 'EUR'
    currencies = ["USD", "AED"]
    date = '2023-01-01'
    api_url = f'https://api.currencyapi.com/v3/historical?apikey=cur_live_hRcnLqKOs4Ut9wH4NoyoMxhIKZnGsVwGYi4603JS&currencies={",".join(currencies)}&base_currency={base_currency}&date={date}'

    response = requests.get(api_url)
    if response.status_code == 200:
        data = response.json()
        print(data)
    else:
        print(f"Failed to retrieve data: {response.status_code}")

if __name__ == "__main__":
    main()
from flask import Flask, request, render_template
import requests

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        base_currency = 'EUR'  # Fixed base currency
        target_currency = request.form['currency']
        date = request.form['date']
        
        api_key = 'cur_live_hRcnLqKOs4Ut9wH4NoyoMxhIKZnGsVwGYi4603JS'
        api_url = f'https://api.currencyapi.com/v3/historical?apikey={api_key}&currencies={target_currency}&base_currency={base_currency}&date={date}'

        response = requests.get(api_url)
        if response.status_code == 200:
            data = response.json()
            rate = data['data'][target_currency]['value']
            return render_template('index.html', target_currency=target_currency, date=date, rate=rate)
        else:
            error_message = f"Failed to retrieve data: {response.status_code}"
            return render_template('index.html', error=error_message)
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)

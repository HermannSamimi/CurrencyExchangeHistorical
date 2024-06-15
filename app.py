from flask import Flask, request, render_template
import requests

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        base_currency = request.form['base_currency']
        currencies = request.form.getlist('currencies')
        date = request.form['date']
        
        api_key = 'cur_live_hRcnLqKOs4Ut9wH4NoyoMxhIKZnGsVwGYi4603JS'
        api_url = f'https://api.currencyapi.com/v3/historical?apikey={api_key}&currencies={",".join(currencies)}&base_currency={base_currency}&date={date}'

        response = requests.get(api_url)
        if response.status_code == 200:
            data = response.json()
            return render_template('index.html', data=data)
        else:
            error_message = f"Failed to retrieve data: {response.status_code}"
            return render_template('index.html', error=error_message)
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)

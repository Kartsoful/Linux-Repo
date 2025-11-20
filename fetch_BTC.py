import requests
import mysql.connector
from datetime import datetime

API_KEY = "YOUR_API_KEY"  # CMC API-avain

# Hae data CoinMarketCapista
url = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest"
params = {
    "symbol": "BTC",
    "convert": "USD"
}
headers = {
    "Accepts": "application/json",
    "X-CMC_PRO_API_KEY": API_KEY
}

response = requests.get(url, headers=headers, params=params)
data = response.json()

price = data['data']['BTC']['quote']['USD']['price']
timestamp = datetime.now()

# Tallenna MySQL:ään
conn = mysql.connector.connect(
    host='localhost',
    user='<user>',
    password='<pass>',
    database='db_name'
)
cursor = conn.cursor()

cursor.execute(
    'INSERT INTO crypto_prices (coin, price_usd, timestamp) VALUES (%s, %s, %s)',
    ('bitcoin', price, timestamp)
)
conn.commit()
cursor.close()
conn.close()

print(f'Data tallennettu: bitcoin ${price:.2f}')


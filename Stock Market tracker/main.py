import os
import requests
from twilio.rest import Client
from dotenv import load_dotenv

load_dotenv()

up="🔺"
down="🔻"

TWILIO_ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
TWILIO_PHONE_FROM = os.getenv("TWILIO_PHONE_FROM")
TWILIO_PHONE_TO = os.getenv("TWILIO_PHONE_TO")

client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"
STOCK_API_KEY = os.getenv("STOCK_API_KEY")
NEWS_API_KEY = os.getenv("NEWS_API_KEY")

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

STOCK_PARAM= {
    "function":"TIME_SERIES_DAILY",
    "symbol": STOCK_NAME ,
    "apikey":STOCK_API_KEY
}
response_stock=requests.get(STOCK_ENDPOINT,params=STOCK_PARAM)
data=response_stock.json()['Time Series (Daily)']
dates=[keys for keys in data.keys()]

STOCK_PRICE_DAY1=float(data[dates[1]]['4. close'])
STOCK_PRICE_DAY2=float(data[dates[0]]['4. close'])

change_percentage=((STOCK_PRICE_DAY1-STOCK_PRICE_DAY2)/STOCK_PRICE_DAY1)*100
if change_percentage>0:
    symbol=f"{up}{round(abs(change_percentage),2)}% rise in price."
else:
    symbol=f"{down}{round(abs(change_percentage),2)}% drop in price."

NEWS_PARAM={
    "apiKey":NEWS_API_KEY,
    "q":COMPANY_NAME,
    "from":dates[1],
    "to":dates[0]
}

response_news=requests.get(NEWS_ENDPOINT,params=NEWS_PARAM)
news=response_news.json()['articles'][0:3]

articles=[f"Headline: {i['title']}.\nDescription: {i['description']}" for i in news]

for article in articles:
    message = client.messages.create(
        body=(
            f"{COMPANY_NAME} Stock Alert!\n"
            f"{symbol}\n{article}"
        ),
        from_=TWILIO_PHONE_FROM,
        to=TWILIO_PHONE_TO,
    )

# config.py
import os

class Config:
    API_KEY = os.getenv('COINMARKETCAP_API_KEY', 'your_coinmarketcap_api_key')
    BASE_URL = 'https://pro-api.coinmarketcap.com/v1/'

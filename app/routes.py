# app/routes.py
from flask import Blueprint, jsonify, render_template
import requests
from flask import current_app as app

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    return render_template('index.html')

@bp.route('/search')
def search():
    return render_template('search.html')

@bp.route('/list')
def list_cryptos():
    return render_template('list.html')

@bp.route('/cryptos', methods=['GET'])
def get_cryptos():
    url = f"{app.config['BASE_URL']}cryptocurrency/listings/latest"
    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': app.config['API_KEY'],
    }
    response = requests.get(url, headers=headers)
    data = response.json()
    return jsonify(data)

@bp.route('/crypto/name/<query>', methods=['GET'])
def get_crypto_by_name(query):
    url = f"{app.config['BASE_URL']}cryptocurrency/quotes/latest"
    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': app.config['API_KEY'],
    }
    params = {
        'slug': query.lower()
    }
    response = requests.get(url, headers=headers, params=params)
    data = response.json()
    return jsonify(data)

@bp.route('/crypto/symbol/<query>', methods=['GET'])
def get_crypto_by_symbol(query):
    url = f"{app.config['BASE_URL']}cryptocurrency/quotes/latest"
    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': app.config['API_KEY'],
    }
    params = {
        'symbol': query.upper()
    }
    response = requests.get(url, headers=headers, params=params)
    data = response.json()
    return jsonify(data)

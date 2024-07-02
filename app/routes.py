# app/routes.py
from flask import Blueprint, render_template, jsonify
import requests
from flask import current_app as app

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    return render_template('index.html')

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

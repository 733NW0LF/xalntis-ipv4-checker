from flask import Flask, render_template, jsonify, request
import requests
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_ip_info')
def get_ip_info():
    try:
        user_ip = request.remote_addr
        response = requests.get(f'http://ipwho.is/{user_ip}?output=json')
        data = response.json()
        return jsonify({
            'ip': data.get('ip'),
            'isp': data.get('connection', {}).get('isp'),
            'city': data.get('city'),
            'region': data.get('region'),
            'country': data.get('country')
        })
    except Exception as e:
        return jsonify({'error': 'Unable to fetch IP information'}), 500

if __name__ == "__main__":
    app.run(debug=False)

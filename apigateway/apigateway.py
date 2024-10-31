# gateway.py
from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# Route til booking-service
@app.route('/api/bookings/<path:path>', methods=['GET', 'POST', 'PUT'])
def booking_service(path):
    url = f'http://booking-service:5001/{path}'
    response = requests.request(method=request.method, url=url, json=request.get_json())
    return jsonify(response.json()), response.status_code

# Route til rengøringsservice
@app.route('/api/cleaning/<path:path>', methods=['GET', 'POST', 'PUT'])
def cleaning_service(path):
    url = f'http://cleaning-service:5003/{path}'
    response = requests.request(method=request.method, url=url, json=request.get_json())
    return jsonify(response.json()), response.status_code

# Route til faktureringsservice
@app.route('/api/billing/<path:path>', methods=['GET', 'POST', 'PUT'])
def billing_service(path):
    url = f'http://billing-service:5002/{path}'
    response = requests.request(method=request.method, url=url, json=request.get_json())
    return jsonify(response.json()), response.status_code

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

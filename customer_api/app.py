from flask import Flask, request, jsonify
import requests
import os

app = Flask(__name__)

BACKEND_API_URL = os.environ['BACKEND_API_URL']

@app.route('/add', methods=['GET'])
def add():
    num1 = request.args.get('num1')
    num2 = request.args.get('num2')
    response = requests.post(f"{BACKEND_API_URL}/add", json={"num1": num1, "num2": num2})
    return jsonify(response.json())

@app.route('/multiply', methods=['GET'])
def multiply():
    num1 = request.args.get('num1')
    num2 = request.args.get('num2')
    response = requests.post(f"{BACKEND_API_URL}/multiply", json={"num1": num1, "num2": num2})
    return jsonify(response.json())

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))
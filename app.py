"""
FILE: app.py
LOCATION: project root

Purpose:
- Run a Flask server
- Serve index.html + predictions.json API
"""

from flask import Flask, jsonify, send_from_directory
import json

app = Flask(__name__, static_url_path='', static_folder='.')

@app.route("/api/predictions")
def api_predictions():
    with open("predictions.json") as f:
        data = json.load(f)
    return jsonify(data)

@app.route("/")
def home():
    return send_from_directory('.', "index.html")

if __name__ == "__main__":
    app.run(port=5000, debug=True)

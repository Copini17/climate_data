from flask import Flask, jsonify, request
import requests
import os
from kaggle.api.kaggle_api_extended import KaggleApi
import zipfile

app = Flask(__name__)

@app.route('/ping', methods=['GET'])
def ping():
    return jsonify({"message": "Pong!"})

@app.route('/download-dataset', methods=['GET'])
def download_dataset():
    dataset = request.args.get('dataset', 'prasad22/weather-data')
    try:
        api = KaggleApi()
        api.authenticate()
        api.dataset_download_files(dataset, path='/root/data/raw', unzip=True)
        return jsonify({"message": f"Dataset {dataset} downloaded and extracted successfully."})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

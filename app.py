from flask import Flask, request, jsonify
from flask_cors import CORS
import numpy as np
from PIL import Image

app = Flask(__name__)
CORS(app) # Enable CORS for all routes

@app.route('/')
def home():
    return "Welcome to the Fruit Freshness Checker API!"

@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return jsonify({'error': 'No file uploaded'}), 400

    file = request.files['file']
    img = Image.open(file.stream).convert('RGB')
    img = img.resize((150, 150))  # Adjust size as needed
    img_array = np.array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0)

    # Mock response (replace with real model predictions)
    is_fresh = np.random.rand() > 0.5
    return jsonify({
        'status': 'Fresh' if is_fresh else 'Rotten',
        'confidence': float(np.random.uniform(0.7, 0.99)),
        'produce': 'Apple',  # Replace with actual prediction
        'indicators': ['Bright color', 'No bruises']
    })

if __name__ == '__main__':
    app.run(debug=True, port=5000)

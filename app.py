# app.py

from flask import Flask, render_template, request
import joblib
from urllib.parse import urlparse

# Load the saved model and vectorizer
model = joblib.load('phishing_url_model.pkl')
vectorizer = joblib.load('tfidf_vectorizer.pkl')

# Initialize Flask app
app = Flask(__name__)

# Function to normalize URLs
def normalize_url(url):
    parsed = urlparse(url)
    domain = parsed.netloc + parsed.path  # Keep domain + path, ignore http/https
    if domain.startswith('www.'):
        domain = domain[4:]
    return domain.lower()

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# Predict route
@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        url = request.form['url']
        normalized_url = normalize_url(url)
        url_transformed = vectorizer.transform([normalized_url])
        prediction = model.predict(url_transformed)
        label = 'Phishing Website' if prediction[0] == 0 else 'Legitimate Website'
        return render_template('index.html', prediction_text=f'Result: {label}')

if __name__ == "__main__":
    app.run(debug=True)

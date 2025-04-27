🛡️ Phishing URL Detection Web App
This project is a simple Flask-based web application that uses an NLP machine learning model to detect whether a given URL is Phishing or Legitimate.

Built with Python, Flask, and Scikit-learn.

📂 Project Structure
/phishing-url-detector
├── app.py                      # Flask Application
├── phishing_url_model.pkl       # Trained ML model (Multinomial Naive Bayes)
├── tfidf_vectorizer.pkl         # TF-IDF Vectorizer
├── requirements.txt             # Required Python packages
└── templates/
    └── index.html               # Frontend HTML Page

🚀 How to Run Locally
1. Clone the repository:
git clone https://github.com/your-username/phishing-url-detector.git
cd phishing-url-detector

2. Install required packages:
pip install -r requirements.txt

3. Run the Flask app:
python app.py

4. Open your browser and visit:
http://127.0.0.1:5000/

🖼️ Features
Input any URL to check if it's phishing or legitimate

URL normalization (handles http/https, www)

Prettified and responsive frontend with basic CSS

Real-time detection with a trained machine learning model

Ready for cloud deployment

☁️ Deploying to Render (Free Cloud Hosting)
Create an account on Render.

Click New Web Service.

Connect your GitHub repository.

Set the following options:

Environment: Python 3

Build Command: (leave blank)

Start Command: python app.py

Deploy!
🛠️ Tech Stack
Python 🐍

Flask 🌐

Scikit-learn 🤖

Joblib 📦

HTML/CSS 🎨

![image](https://github.com/user-attachments/assets/5dd1c836-f616-423a-ada3-7c50590b39c3)

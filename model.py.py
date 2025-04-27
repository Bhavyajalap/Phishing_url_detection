# phishing_url_detection.py

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import classification_report, accuracy_score
import joblib

# 1. Load dataset
file_path = 'phishing_site_urls.csv'  # Change path if needed
df = pd.read_csv(file_path)

# 2. Preprocessing - Encode Labels ('bad' -> 0, 'good' -> 1)
label_encoder = LabelEncoder()
df['Label'] = label_encoder.fit_transform(df['Label'])

# 3. Split data
X_train, X_test, y_train, y_test = train_test_split(
    df['URL'], df['Label'], test_size=0.2, random_state=42, stratify=df['Label']
)

# 4. Feature Extraction - TF-IDF
vectorizer = TfidfVectorizer(token_pattern=r'[A-Za-z0-9]+')
X_train_tfidf = vectorizer.fit_transform(X_train)
X_test_tfidf = vectorizer.transform(X_test)

# 5. Model - Multinomial Naive Bayes
model = MultinomialNB()
model.fit(X_train_tfidf, y_train)

# 6. Evaluate
predictions = model.predict(X_test_tfidf)
accuracy = accuracy_score(y_test, predictions)
report = classification_report(y_test, predictions)

print("\n=== Model Evaluation ===")
print(f"Accuracy: {accuracy * 100:.2f}%")
print(report)

# 7. Save model and vectorizer
joblib.dump(model, 'phishing_url_model.pkl')
joblib.dump(vectorizer, 'tfidf_vectorizer.pkl')

print("\nModel and Vectorizer saved!")

# 8. Prediction function
def predict_url(url):
    loaded_model = joblib.load('phishing_url_model.pkl')
    loaded_vectorizer = joblib.load('tfidf_vectorizer.pkl')
    url_transformed = loaded_vectorizer.transform([url])
    prediction = loaded_model.predict(url_transformed)
    label = 'Phishing' if prediction[0] == 0 else 'Legitimate'
    return label

# Example Usage
if __name__ == "__main__":
    test_url = "google.com"
    result = predict_url(test_url)
    print(f"\nPrediction for '{test_url}': {result}")

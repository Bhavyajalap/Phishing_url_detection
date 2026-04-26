from flask import Flask, render_template, request, redirect
import joblib
import numpy as np
from utils.feature_extractor import extract_features
from utils.explain import generate_explanation

app = Flask(__name__)

# Load model
model = joblib.load("model.pkl")

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        url = request.form.get("url")

        if not url or len(url.strip()) == 0:
            return render_template("index.html", error="Please enter a valid URL")

        # Feature extraction
        features = extract_features(url)
        features = np.array(features).reshape(1, -1)

        # Prediction
        prob = model.predict_proba(features)[0][1]
        risk_score = int(prob * 100)

        # Labeling
        if risk_score < 30:
            label = "Safe"
        elif risk_score < 70:
            label = "Suspicious"
        else:
            label = "Malicious"

        # Explanation
        explanation = generate_explanation(url)

        return render_template(
            "index.html",
            url=url,
            risk_score=risk_score,
            label=label,
            explanation=explanation
        )

    return render_template("index.html")


@app.route("/feedback", methods=["POST"])
def feedback():
    url = request.form.get("url")
    feedback = request.form.get("feedback")

    with open("feedback.csv", "a") as f:
        f.write(f"{url},{feedback}\n")

    return redirect("/")


@app.route("/dashboard")
def dashboard():
    try:
        with open("feedback.csv", "r") as f:
            data = f.readlines()

        total = len(data)
        correct = sum(1 for d in data if "correct" in d)
        incorrect = sum(1 for d in data if "incorrect" in d)

    except:
        total = correct = incorrect = 0

    return render_template(
        "dashboard.html",
        total=total,
        correct=correct,
        incorrect=incorrect
    )


if __name__ == "__main__":
    app.run(debug=True)

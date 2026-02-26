from flask import Flask, render_template, request
import joblib
import pandas as pd
import matplotlib.pyplot as plt

app = Flask(__name__)
model = joblib.load("models/best_model.pkl")
features = [
    "PM2.5",
    "PM10",
    "NO",
    "NO2",
    "NOx",
    "NH3",
    "CO",
    "SO2",
    "O3"
]
def get_aqi_category(aqi):
    if aqi <= 50:
        return "Good"
    elif aqi <= 100:
        return "Moderate"
    elif aqi <= 200:
        return "Unhealthy"
    elif aqi <= 300:
        return "Very Unhealthy"
    else:
        return "Hazardous"
def generate_feature_importance():
    if hasattr(model, "feature_importances_"):
        importances = model.feature_importances_
        plt.figure(figsize=(6,4))
        plt.barh(features, importances[:len(features)])
        plt.title("Feature Importance")
        plt.tight_layout()
        plt.savefig("static/feature_importance.png")
        plt.close()
df = pd.read_csv("models/model_results.csv")
chart_labels = df["model"].tolist()
chart_values = df["rmse"].tolist()
@app.route("/", methods=["GET", "POST"])
def home():
    prediction = None
    category = None
    if hasattr(model, "feature_importances_"):
        feature_labels = features
        feature_values = model.feature_importances_[:len(features)].tolist()
    else:
        feature_labels = []
        feature_values = []
    if request.method == "POST":
        values = [float(request.form[f]) for f in features]
        prediction = model.predict([values])[0]
        category = get_aqi_category(prediction)
        generate_feature_importance()
    return render_template(
        "index.html",
        features=features,
        prediction=prediction,
        category=category,
        chart_labels=chart_labels,
        chart_values=chart_values,
        feature_labels=feature_labels,
        feature_values=feature_values
    )
if __name__ == "__main__":
    app.run(debug=True)
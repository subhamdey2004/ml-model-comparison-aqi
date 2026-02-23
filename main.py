from src.preprocessing import load_data, clean_data
from src.feature_engineering import prepare_features
from src.train_models import get_models
from src.evaluate_models import evaluate
from sklearn.model_selection import train_test_split
import pandas as pd
import joblib

print("LOADING DATASET...")

df = load_data("data/raw/aqi_dataset.csv")

print("CLEANING DATA...")

df = clean_data(df)

df.to_csv("data/processed/cleaned_data.csv", index=False)

print("PREPARING FEATURES...")

X, y = prepare_features(df)

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

models = get_models()

best_score = -999
best_model = None

results = []

print("\nTRAINING MODELS...\n")

for name, model in models.items():

    print(f"Training: {name}")

    model.fit(X_train, y_train)

    rmse, r2 = evaluate(model, X_test, y_test)

    print(f"{name} -> RMSE: {rmse:.2f} | R2: {r2:.4f}")

    results.append({
        "model": name,
        "rmse": rmse,
        "r2": r2
    })

    if r2 > best_score:
        best_score = r2
        best_model = model


results_df = pd.DataFrame(results)

results_df.to_csv("models/model_results.csv", index=False)

print("\nModel results saved to models/model_results.csv")


joblib.dump(best_model, "models/best_model.pkl")

print("Best model saved as models/best_model.pkl")

print("\nTRAINING COMPLETED SUCCESSFULLY.")

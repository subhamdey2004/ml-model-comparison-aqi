import pandas as pd

def prepare_features(df):
    if 'City' in df.columns:
        df = df.drop(columns=['City'])
    if 'Datetime' in df.columns:
        df['Datetime'] = pd.to_datetime(df['Datetime'])
        df['month'] = df['Datetime'].dt.month
        df['day'] = df['Datetime'].dt.day
        df = df.drop(columns=['Datetime'])
    selected_features = [
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
    X = df[selected_features]
    y = df["AQI"]
    return X, y

import pandas as pd

def load_data(path):
    df = pd.read_csv(path)
    return df
def clean_data(df):
    df = df.dropna()
    if 'AQI_Bucket' in df.columns:
        df = df.drop(columns=['AQI_Bucket'])
        return df

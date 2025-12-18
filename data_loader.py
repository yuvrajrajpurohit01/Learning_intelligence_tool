import pandas as pd

def load_data(file_path):
    if not file_path.endswith(".csv"):
        raise ValueError("Only CSV files are supported")
    return pd.read_csv(file_path)

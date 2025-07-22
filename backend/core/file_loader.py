import pandas as pd
import json

def load_financial_data(file):
    if file.name.endswith(".csv"):
        df = pd.read_csv(file)
    elif file.name.endswith(".xlsx") or file.name.endswith(".xls"):
        df = pd.read_excel(file)
    elif file.name.endswith(".json"):
        df = pd.read_json(file)
    else:
        raise ValueError("Unsupported file format")
    return df


def normalize_table(df: pd.DataFrame) -> str:
    """
    Converts DataFrame to normalized string rows for embedding.
    """
    return "\n".join(df.astype(str).apply(lambda row: " | ".join(row), axis=1))

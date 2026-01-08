import pandas as pd

def flatten_table(df: pd.DataFrame) -> str:
    """
    Convert a pandas DataFrame (table) into string
    """
    return df.to_csv(index=False)

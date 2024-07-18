import pandas as pd

def pivotTable(df: pd.DataFrame) -> pd.DataFrame:
    return df.pivot(columns=['city'], index='month', values='temperature')
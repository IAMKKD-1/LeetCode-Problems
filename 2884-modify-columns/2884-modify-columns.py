import pandas as pd

def modifySalaryColumn(df: pd.DataFrame) -> pd.DataFrame:
    # df.salary = df.salary*2
    df.salary = df.salary.apply(lambda x: 2*x)
    return df
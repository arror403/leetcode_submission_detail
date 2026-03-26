import pandas as pd

def dropMissingData(students: pd.DataFrame) -> pd.DataFrame:
    # students.dropna(axis='name', inplace=True)

    return students.dropna()
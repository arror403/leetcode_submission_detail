import pandas as pd

def rising_temperature(weather: pd.DataFrame) -> pd.DataFrame:
    weather.sort_values(by='recordDate', inplace=True)
    res=[]

    for a,b in pairwise(zip(weather['id'], weather['temperature'])):
        if b[1]>a[1]:
            res.append(b[0])


    return pd.DataFrame({'id': res})
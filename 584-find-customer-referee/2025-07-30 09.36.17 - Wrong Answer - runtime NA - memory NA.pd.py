import pandas as pd

def find_customer_referee(customer: pd.DataFrame) -> pd.DataFrame:
    res=set()

    for n,i in zip(customer['name'], customer['referee_id']):
        # print(n,i)
        if ((i is pd.NA) or (i!=2)):
            res.add(n)

    res=list(res)
    return pd.DataFrame({"name":res})
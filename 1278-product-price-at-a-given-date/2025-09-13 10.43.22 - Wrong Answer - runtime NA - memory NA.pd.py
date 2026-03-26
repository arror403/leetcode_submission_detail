import pandas as pd

def price_at_given_date(products: pd.DataFrame) -> pd.DataFrame:
    t=date.fromisoformat('2019-08-16')
    p=set(products['product_id'])
    d=defaultdict(int)

    products.sort_values(by=['change_date'])

    for _,r in products.iterrows():
        if date.fromisoformat(str(r['change_date'])[:10])>t: break
        d[r['product_id']]=r['new_price']

    for k in (p-set(d.keys())): d[k]=10

    # print(d)

    return pd.DataFrame({'product_id': d.keys(), 'price': d.values()})
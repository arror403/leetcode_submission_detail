import pandas as pd

def monthly_transactions(transactions: pd.DataFrame) -> pd.DataFrame:
    d={}

    for _,r in transactions.iterrows():
        t=str(r['trans_date'].year)+'-'+str(r['trans_date'].month).zfill(2)+r['country']

        if t not in d: d[t]=[t[:7], r['country'], 0, 0, 0, 0]

        d[t][2]+=1

        d[t][4]+=r['amount']

        if r['state']=='approved':
            d[t][3]+=1
            d[t][5]+=r['amount']


    return pd.DataFrame(d.values(), columns=['month', 'country', 'trans_count', 'approved_count', 'trans_total_amount', 'approved_total_amount'])
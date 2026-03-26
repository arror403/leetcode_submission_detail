import pandas as pd

def find_employees(employees: pd.DataFrame) -> pd.DataFrame:
    left_mid=set(employees['manager_id'])-set(employees['employee_id'])
    res=[]

    for eid, mid, s in zip(employees['employee_id'], employees['manager_id'], employees['salary']):
        if (mid in left_mid) and s<30000:
            res.append(eid)


    return pd.DataFrame({'employee_id':sorted(res)})
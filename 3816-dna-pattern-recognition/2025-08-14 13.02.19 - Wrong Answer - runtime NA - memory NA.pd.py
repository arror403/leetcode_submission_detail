import pandas as pd

def analyze_dna_patterns(samples: pd.DataFrame) -> pd.DataFrame:
    s=samples['dna_sequence']
    
    c1=[1 if c.startswith("ATG") else 0 for c in s]
    samples['has_start']=c1

    c2=[]
    for c in s:
        if c.endswith("TAA") or c.endswith("TAG") or c.endswith("TGA "):
            c2.append(1)
        else:
            c2.append(0)
    samples['has_stop']=c2

    c3=[1 if "ATAT" in c else 0 for c in s]
    samples['has_atat']=c3

    c4=[0]*len(s)
    i=0
    for c in s:
        for _,g in groupby(c):
            if len(list(g))>=3:
                c4[i]=1
                break
        i+=1
    samples['has_ggg']=c4
    # print(c1,c2,c3,c4)

    return samples.sort_values('sample_id')
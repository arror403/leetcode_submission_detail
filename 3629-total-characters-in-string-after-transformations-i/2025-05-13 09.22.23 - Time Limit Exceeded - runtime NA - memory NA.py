class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        d=Counter(s)
        # print(d)

        for _ in range(t):
            tmp=Counter()
            for i in range(25):
                if d[chr(97+i)]:
                    tmp[chr(98+i)]=d[chr(97+i)]
                    # del tmp[chr(97+i)]
            if d['z']:    
                tmp['a']=d['z']
                tmp['b']+=d['z']
            # print(tmp)
            d=tmp


        return d.total()%(10**9+7)
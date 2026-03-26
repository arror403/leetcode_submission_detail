class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        b=Counter(s)
        r=Counter(g)
        res=0
        # print(b,r)
        for k,v in r.items():
            if k in b.keys():
                if v<=b[k]:
                    res+=v
                else:
                    res+=b[k]

        return res
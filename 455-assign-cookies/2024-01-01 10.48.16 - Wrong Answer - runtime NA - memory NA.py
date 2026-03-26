class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        # if len(s)==0: return 0
        b=Counter(s)
        r=Counter(g)
        res=0

        for k,v in r.items():
            if k in b.keys() and v<=b[k]:
                res+=v

        return res
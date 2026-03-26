class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        t=list(map(lambda y:y in [(0,1),(1,0)], pairwise(map(lambda x:x%2, nums))))

        if all(t): return [True]*len(queries)

        m=[i for i,v in enumerate(t) if v==False]
        res=[]

        for a,b in queries:
            if (b-a)==0:
                res+=[True]
            elif (b-a)==1:
                res+=[t[b-a+1]]
            else:
                res+=[(b-1)<m[0] or m[-1]<a]

        return res
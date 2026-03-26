class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        d=defaultdict(int)
        res=0

        for a,b in points:
            d[b]+=1

        t=[(x*x-x)//2 for x in d.values()]

        for p,q in combinations(t,2):
            res+=(p*q)%(10**9+7)


        return res
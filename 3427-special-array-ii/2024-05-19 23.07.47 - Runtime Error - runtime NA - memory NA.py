class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        t=map(lambda y:y in [(0,1),(1,0)], pairwise(map(lambda x:x%2, nums)))
        m=[i for i,v in enumerate(t) if v==False]
        return [(m[0]>b-1 or a>m[-1]) for a,b in queries]
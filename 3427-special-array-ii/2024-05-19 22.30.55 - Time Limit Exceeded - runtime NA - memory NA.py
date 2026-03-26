class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        t=list(map(lambda y:y in [(0,1),(1,0)], pairwise(map(lambda x:x%2, nums))))

        return [all(t[a:b]) for a,b in queries]
            
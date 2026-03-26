class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        t=[x[1] for x in trust]
        if len(set(t))==1 and len(t)==(n-1):
            return t[0]
        else:
            return -1
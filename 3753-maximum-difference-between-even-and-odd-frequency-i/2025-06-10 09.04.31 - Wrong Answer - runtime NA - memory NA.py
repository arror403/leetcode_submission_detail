class Solution:
    def maxDifference(self, s: str) -> int:
        m=[[],[]]
        for f in Counter(s).values(): m[f%2]+=[f]
        return (max(m[1])-max(m[0]))
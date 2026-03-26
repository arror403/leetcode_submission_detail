class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        return list(set(t)-set(s))[0]
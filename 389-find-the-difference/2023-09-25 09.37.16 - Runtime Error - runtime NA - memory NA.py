class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        return [i for i in t if i not in s][0]
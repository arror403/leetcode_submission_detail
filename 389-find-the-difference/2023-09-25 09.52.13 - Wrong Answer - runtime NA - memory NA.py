class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        return next((t[i] for i, (x, y) in enumerate(zip(sorted(s), sorted(t))) if x != y), t[-1])
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        return 0 if sorted(s)==sorted(t) else sorted(Counter(s).values())==sorted(Counter(t).values())
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        return s==re.search(p,s).group(0)
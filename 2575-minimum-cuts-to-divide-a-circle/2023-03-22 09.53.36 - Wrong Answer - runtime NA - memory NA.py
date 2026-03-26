class Solution:
    def numberOfCuts(self, n: int) -> int:
        if n%2==0: return int(n/2)
        else: return n
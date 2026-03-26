class Solution:
    def getSum(self, a: int, b: int) -> int:
        if a==0: return b
        if b==0: return a
        else: return int(log(exp(a) * exp(b)))
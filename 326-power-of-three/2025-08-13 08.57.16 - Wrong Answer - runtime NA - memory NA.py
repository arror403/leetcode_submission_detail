class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        return n>0 and log(n,3)==int(log(n,3))
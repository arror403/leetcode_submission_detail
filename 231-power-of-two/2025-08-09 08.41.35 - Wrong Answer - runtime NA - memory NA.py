class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n>0 and sqrt(n)==int(sqrt(n))
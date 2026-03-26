class Solution:
    def arrangeCoins(self, n: int) -> int:
        for i in range(1,n+1):
            if self.helper(i)<n: continue
            return i-1
        
        
    def helper(self, x):
        return int((1+x)*x/2)
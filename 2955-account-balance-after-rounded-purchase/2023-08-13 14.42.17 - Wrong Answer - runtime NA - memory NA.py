class Solution:
    def accountBalanceAfterPurchase(self, p: int) -> int:
        if p==100: return 0
        elif p==0: return 100
        else: return min(100-(p//10)*10 , 100-(p//10+1)*10)
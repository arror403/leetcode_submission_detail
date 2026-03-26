class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        b=[]
        for i in range(0,len(prices)):
            for j in range(i,len(prices)):
                b.append(prices[j]-prices[i])
        if max(b)<0:
            return 0
        else:
            return max(b)
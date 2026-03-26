class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        L = len(prices)
        if k >= L//2: 
            profit = 0
            for i in range(1, L):
                # as long as there is a price gap, we gain a profit
                if prices[i] > prices[i-1]: 
                    profit += prices[i] - prices[i-1]

            return profit
 
        t=[[0]*(L) for _ in range(k+1)]
        for i in range(1, k+1):
            tmpMax = -prices[0]
            for j in range(L):
                t[i][j] = max(t[i][j-1], prices[j] + tmpMax)
                tmpMax =  max(tmpMax, t[i-1][j-1] - prices[j])
        

        return t[k][L-1]
class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        arr = [[i*j for i in range(1,n+1)] for j in range(1,m+1)]
        arr = reduce(lambda x,y :x+y ,arr)
        return sorted(arr)[k-1]
        # return 0
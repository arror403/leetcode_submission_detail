class Solution:
    def rob(self, nums: List[int]) -> int:

        def Rob(n, i):
            if (i<0): return 0
            return max(Rob(n,i-2)+n[i],Rob(n,i-1))

        return Rob(nums,len(nums)-1)


        
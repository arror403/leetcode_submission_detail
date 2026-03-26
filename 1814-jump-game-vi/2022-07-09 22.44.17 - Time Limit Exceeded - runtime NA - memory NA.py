class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        
#         s=0
#         i=0
#         n=len(nums)
#         while 1:
#             if i==n-1:
#                 break
#             s+=max(nums[i:i+k])
#             i=nums.index(max(nums[i:i+k]))   

#         return s
        n = len(nums)
        dp = [-math.inf] * n
        dp[0] = nums[0]
        for i in range(1, n):
            for j in range(max(i-k, 0), i):
                dp[i] = max(dp[i], dp[j] + nums[i])
        return dp[n-1]
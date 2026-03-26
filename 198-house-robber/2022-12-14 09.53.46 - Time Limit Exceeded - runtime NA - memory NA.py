class Solution:
    def rob(self, nums: List[int]) -> int:

        def Rob(nums, i):
            if (i<0):
                return 0
            return max(Rob(nums, i-2)+nums[i], Rob(nums, i-1))

        return Rob(nums, len(nums)-1)
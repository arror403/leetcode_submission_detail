class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        return self.dp(nums, target, len(nums)-1, 0)


    def dp(self, m, t, index, curr_sum):
        # Base Cases
        if index < 0: return curr_sum == t
        # Decisions
        positive = self.dp(m, t, index-1, curr_sum + m[index])
        negative = self.dp(m, t, index-1, curr_sum - m[index])
        
        return positive + negative
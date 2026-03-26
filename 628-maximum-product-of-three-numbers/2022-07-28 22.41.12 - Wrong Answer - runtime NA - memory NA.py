class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        return sorted(nums)[-1]*sorted(nums)[-2]*sorted(nums)[-3]
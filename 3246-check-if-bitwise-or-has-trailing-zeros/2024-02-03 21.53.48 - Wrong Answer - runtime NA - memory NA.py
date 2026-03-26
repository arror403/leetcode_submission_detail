class Solution:
    def hasTrailingZeros(self, nums: List[int]) -> bool:
        return any(i%2==0 for i in nums)
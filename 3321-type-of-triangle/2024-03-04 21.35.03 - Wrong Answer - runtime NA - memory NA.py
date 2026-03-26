class Solution:
    def triangleType(self, nums: List[int]) -> str:
        return ["equilateral","isosceles","scalene"][len(set(nums))-1]
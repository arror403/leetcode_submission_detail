class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        return [i for i,v in enumerate(nums) if v==target] or [-1,-1]
class Solution:
    def countValidSelections(self, nums: List[int]) -> int:
        m=[i for i,v in enumerate(nums) if v==0]

        return sum(sum(nums[:e])==sum(nums[e+1:]) for e in m)*2
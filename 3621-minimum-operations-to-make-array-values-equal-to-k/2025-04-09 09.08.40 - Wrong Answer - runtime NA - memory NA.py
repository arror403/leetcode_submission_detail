class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        if len(set(nums))==1:
            if nums[0]==k:
                return 0

        t=sum(v>k for v in set(nums))


        return t if t else -1
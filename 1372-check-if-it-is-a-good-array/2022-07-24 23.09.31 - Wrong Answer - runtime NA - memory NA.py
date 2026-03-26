class Solution:
    def isGoodArray(self, nums: List[int]) -> bool:
        f=False
        nums.sort()
        for i in nums:
            if i%nums[0]==0:
                continue
            else:
                f=True
                break
        return f
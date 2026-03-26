class Solution:
    def isGoodArray(self, nums: List[int]) -> bool:
        f=False
        if len(nums)==1 and nums[0]==1:
            f=True
        elif min(nums)==1:
            f=True
        else:
            nums.sort()
            for i in nums:
                if i%nums[0]==0:
                    continue
                else:
                    f=True
                    break
        return f
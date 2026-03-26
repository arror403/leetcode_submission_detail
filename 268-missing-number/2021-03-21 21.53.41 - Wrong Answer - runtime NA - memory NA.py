class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        b=-1
        for i in range(0,len(nums)-1):
            if nums[0]!=0:
                b=0
                break
            elif nums[i]!=nums[i+1]-1:
                b=nums[i+1]-1
        if b==-1:
            return nums[-1]+1
        else:
            return b
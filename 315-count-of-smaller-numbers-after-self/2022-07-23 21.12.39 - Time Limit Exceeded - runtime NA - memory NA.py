class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        res=[0]*len(nums)
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]>nums[j]:
                    res[i]+=1
                    
        return res
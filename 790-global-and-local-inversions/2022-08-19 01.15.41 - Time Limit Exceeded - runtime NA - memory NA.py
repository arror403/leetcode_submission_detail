class Solution:
    def isIdealPermutation(self, nums: List[int]) -> bool:
        l,g=0,0
        for i in range(len(nums)-1):
            if nums[i] > nums[i+1]:
                l+=1
                
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]>nums[j]:
                    g+=1
                    
        return l==g
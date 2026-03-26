class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        b=[]
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]==nums[j]:
                    b.append(nums[i])
                    
        return b
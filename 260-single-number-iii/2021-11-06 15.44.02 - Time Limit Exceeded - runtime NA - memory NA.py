class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        b=[]
        for i in range(len(nums)):
            f=0
            for j in range(len(nums)):
                if nums[i]==nums[j] and i!=j:
                    f=1
                    break
            if f==0:
                b.append(nums[i])
        return b
            
                
                
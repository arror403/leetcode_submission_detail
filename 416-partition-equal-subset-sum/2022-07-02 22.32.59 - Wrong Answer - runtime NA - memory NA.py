class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        b=[]
        f=0
        for i in nums:
            b.append(nums)
            nums=nums[1:]+nums[:1]
            
        x=int(len(nums)/2)
        
        for i in range(1,x+1):
            for j in b:
                if sum(j[:i])==sum(j[i:]):
                    f=1
                    break
                    
        if f:
            return 1
        else:
            return 0
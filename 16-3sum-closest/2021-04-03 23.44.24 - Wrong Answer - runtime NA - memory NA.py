class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        # b=[]
        min=9999
        for i in range(1,len(nums)-1):
            tmp=nums[i-1]+nums[i]+nums[i+1]
            # b.append(tmp) 
            if (target-tmp)<min:
                x=i
        
        return x
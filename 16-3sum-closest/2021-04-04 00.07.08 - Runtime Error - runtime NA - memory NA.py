class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        b=[]
        nums.sort()
        # print (nums)
        for i in range(len(nums)-2):
            for j in range(i+1,len(nums)-1):
                for k in range(j+1,len(nums)):
                    tmp=nums[i]+nums[j]+nums[k]
                    if not(tmp in b): b.append(tmp)
        
        b.sort()
        for i in b:
            if i>=target:
                x=i
                break
        
        # print (b)
        
        return x
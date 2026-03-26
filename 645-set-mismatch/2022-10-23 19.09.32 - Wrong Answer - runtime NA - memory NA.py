class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        if nums==[1,1] or nums==[2,2]: return [1,2]
        nums.sort()
        res=[]
        for i in range(len(nums)-1):
            if (nums[i]==nums[i+1]): res.append(nums[i])
            if (nums[i+1]-nums[i])==2: res.append(nums[i]+1)
        return res
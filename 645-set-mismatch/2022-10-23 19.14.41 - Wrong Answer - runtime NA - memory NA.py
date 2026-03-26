class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        nums.sort()
        print(nums)
        res=[]
        for i in range(len(nums)-1):
            if (nums[i]==nums[i+1]): res.append(nums[i])
        for i in range(1,len(nums)+1):
            if i!=nums[i-1]: 
                res.append(i)
                break
        return res
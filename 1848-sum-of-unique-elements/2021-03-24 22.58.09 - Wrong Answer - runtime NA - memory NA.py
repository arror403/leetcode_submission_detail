class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        i=0
        sum=0
        nums.sort()
        while i<=len(nums)-2:
            if nums[i]==nums[i+1]:
                i+=2
            else:
                sum+=nums[i]
                i+=1
                
        # print (nums)
        
        return(sum+nums[-1])
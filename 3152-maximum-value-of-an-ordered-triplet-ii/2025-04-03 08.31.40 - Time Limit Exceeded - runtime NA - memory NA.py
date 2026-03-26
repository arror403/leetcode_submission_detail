class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        prefix_max=[]
        suffix_max=[]
        res=0

        for i in range(len(nums)):
            prefix_max.append(max(nums[:i+1]))
            suffix_max.append(max(nums[i:]))

        for i in range(1,len(nums)-1):
            res=max(res, (prefix_max[i-1]-nums[i])*suffix_max[i+1])


        return res
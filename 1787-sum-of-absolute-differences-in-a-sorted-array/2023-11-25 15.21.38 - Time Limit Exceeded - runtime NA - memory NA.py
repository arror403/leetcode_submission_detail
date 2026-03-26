class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        # return [ for i,v in enumerate(nums)]

        res=[]

        l=len(nums)

        for i,v in enumerate(nums):
            res.append(sum(nums[i:])-(l-i)*v + i*v-sum(nums[:i]))

        return res
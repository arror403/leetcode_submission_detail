class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        if len(nums)<=5: return sum(nums)/k
        res=-inf
        for i in range(len(nums)-k+1):
            # print(nums[i:i+k])
            tmp=sum(nums[i:i+k])/k
            if tmp>res: res=tmp

        return res
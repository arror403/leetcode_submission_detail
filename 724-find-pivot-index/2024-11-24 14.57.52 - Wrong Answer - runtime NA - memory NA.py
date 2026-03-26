class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        l,r=0,sum(nums[1:])

        for i in range(len(nums)-1):
            if l==r:
                return i
            else:
                l+=nums[i]
                r-=nums[i+1]


        return -1
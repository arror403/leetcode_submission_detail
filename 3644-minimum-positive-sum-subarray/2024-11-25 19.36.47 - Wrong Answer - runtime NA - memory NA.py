class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        L=len(nums)
        return min([w for i in range(L-l) if (w:=sum(nums[i:i+l]))>0]
                  +[w for i in range(L-r) if (w:=sum(nums[i:i+r]))>0], default=-1)
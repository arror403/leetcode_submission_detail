class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        L=len(nums)+1
        # print([sum(nums[i:i+l]) for i in range(L-l)],[sum(nums[i:i+r]) for i in range(L-r)])

        return min([w for i in range(L-l) if (w:=sum(nums[i:i+l]))>0]
                  +[e for i in range(L-r) if (e:=sum(nums[i:i+r]))>0], default=-1)
class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        L = len(nums)

        return sum(1 for i in range(1, L+1) for j in range(L-i+1) if 2*nums[j:j+i].count(target) > i)
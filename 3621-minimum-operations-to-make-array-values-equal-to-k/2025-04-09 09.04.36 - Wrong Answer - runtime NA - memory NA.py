class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        return t if (t:=sum(v>k for v in set(nums))) else -1
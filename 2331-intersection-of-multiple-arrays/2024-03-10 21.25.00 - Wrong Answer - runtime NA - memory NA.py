class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        return reduce(lambda x,y: x&y, [set(i) for i in nums])
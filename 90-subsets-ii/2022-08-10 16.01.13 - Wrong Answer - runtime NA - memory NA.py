class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        return dict.fromkeys([j for i in range(len(nums)+1) for j in itertools.combinations(nums,i)])
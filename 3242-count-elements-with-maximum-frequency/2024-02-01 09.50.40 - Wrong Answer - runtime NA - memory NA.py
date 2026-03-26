class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        c=list(Counter(nums).values())
        return sum(i for i in c if i==c[0])
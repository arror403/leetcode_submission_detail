class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        S=sum(nums)
        p=list(accumulate(nums))


        return sum(1 for x in p if x>=(S-x))-1
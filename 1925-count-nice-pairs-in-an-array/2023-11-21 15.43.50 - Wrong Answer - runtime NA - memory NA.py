class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        # print(Counter([n-int(str(n)[::-1]) for n in nums]))

        return int(sum([(x*(x-1)/2) for x in Counter([n-int(str(n)[::-1]) for n in nums]).values()]))
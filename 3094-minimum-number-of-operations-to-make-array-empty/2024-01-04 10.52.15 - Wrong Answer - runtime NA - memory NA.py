class Solution:
    def minOperations(self, nums: List[int]) -> int:
        res=0

        for x in Counter(nums).values():
            if x%3==0: res+=x//3
            elif x%2==0: res+=x//2
            else: return -1

        return res
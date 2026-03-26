class Solution:
    def maximumProduct(self, nums: List[int], k: int) -> int:
        for i in range(k):
            nums[nums.index(min(nums))]+=1
            k-=1
        return reduce(lambda a,b:a*b,nums)%(10**9+7)
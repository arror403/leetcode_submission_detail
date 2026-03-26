class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if all([i==0 for i in nums]): return nums

        p=reduce(lambda x,y:x*y, [i for i in nums if i!=0])

        if (nums.count(0)>0):
            return [p if x==0 else 0 for x in nums]
        else:
            return [p//x if x!=0 else p for x in nums]
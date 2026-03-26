class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        s=set(i for i in nums if i>0)
        if not s: return 1

        t=set(range(1,max(s)+1))

        # print(s,t)

        return min(t-s) if (t-s) else max(s)+1
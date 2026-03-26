class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        d={v:i for i,v in enumerate(nums)}
        return [q[1] for q in sorted([[d[c],c] for c in sorted(nums,reverse=1)[:k]], key=lambda x:x[0])]
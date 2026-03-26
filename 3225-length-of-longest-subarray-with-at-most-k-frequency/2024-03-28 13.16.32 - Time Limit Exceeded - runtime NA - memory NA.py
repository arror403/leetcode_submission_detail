class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        L=len(nums)
        d=Counter()
        res=[]
        start=0
        
        for end in range(L):
            d[nums[end]]+=1
            while any(x>k for x in d.values()):
                d[nums[start]]-=1
                if d[nums[start]]==0: del d[nums[start]]
                start+=1
            
            res.append(end-start+1)
            
        return max(res, default=0)
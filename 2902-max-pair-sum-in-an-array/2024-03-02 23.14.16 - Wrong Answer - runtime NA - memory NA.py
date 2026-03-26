class Solution:
    def maxSum(self, nums: List[int]) -> int:
        res=[]
        for i in nums:
            if i<10 and nums.count(i)>1:
                res.append(2*i)
        
        for i in nums:
            if i<10: continue
            tmp=int(str(i)[::-1])
            if tmp in nums:
                res.append(i+tmp)

        return -1 if len(res)==0 else max(res)
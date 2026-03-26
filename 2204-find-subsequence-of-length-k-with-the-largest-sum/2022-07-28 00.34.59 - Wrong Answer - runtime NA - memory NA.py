class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        m=sorted(nums)[len(nums)-k:len(nums)]
        res=[]
        
        for i in nums:
            if i in m and len(res)!=len(m):
                res.append(i)
                    
        return res
        
        
        
#         i=0
#         tmp=float("-inf")
#         res=[]
#         while (i+k)<=len(nums):
#             if sum(nums[i:i+k])>tmp:
#                 res=nums[i:i+k]
#             i+=1
                
#         return res




        # return sorted(nums)[len(nums)-k:len(nums)]
            
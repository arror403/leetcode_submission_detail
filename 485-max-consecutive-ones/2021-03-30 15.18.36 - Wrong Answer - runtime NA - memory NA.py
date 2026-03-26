class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        tmp=0
        b=[]
        for i in nums:
            if i==1:
                tmp+=1
            elif i==0:
                b.append(tmp)
                tmp=0
        if len(b)==0:return 0
        
        else: return (max(b))
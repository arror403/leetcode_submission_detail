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
        return (max(b))
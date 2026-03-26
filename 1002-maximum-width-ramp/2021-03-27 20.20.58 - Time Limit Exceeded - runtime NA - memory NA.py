class Solution:
    def maxWidthRamp(self, A: List[int]) -> int:
        b=[]
        for i in range(len(A)):
            for j in range(i+1,len(A)):
                if A[i]<=A[j]:
                    b.append(j-i)
        if len(b)==0: return 0
        else: return max(b)
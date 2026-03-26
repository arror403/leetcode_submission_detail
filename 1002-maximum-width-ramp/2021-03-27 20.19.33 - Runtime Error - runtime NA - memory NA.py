class Solution:
    def maxWidthRamp(self, A: List[int]) -> int:
        b=[]
        for i in range(len(A)):
            for j in range(i+1,len(A)):
                if A[i]<=A[j]:
                    b.append(j-i)
                    
        return max(b)
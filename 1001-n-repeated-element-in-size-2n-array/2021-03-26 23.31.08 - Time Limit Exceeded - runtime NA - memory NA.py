class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        for i in range(len(A)):
            for j in range(len(A)):
                if (i!=j) & (A[i]==A[j]):
                    b=A[i]
                    break
            
        return b
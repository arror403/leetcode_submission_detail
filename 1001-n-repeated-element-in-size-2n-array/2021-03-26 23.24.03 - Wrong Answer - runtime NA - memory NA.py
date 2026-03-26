class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        x=int(len(A)/2)
        A.sort()
        if A[0]==A[1]:
            return A[0]
        else:
            return A[-1]
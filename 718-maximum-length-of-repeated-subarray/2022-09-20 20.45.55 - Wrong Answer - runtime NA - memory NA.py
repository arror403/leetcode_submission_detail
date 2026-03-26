class Solution:
    def findLength(self, A: List[int], B: List[int]) -> int:
        if (len(A) < len(B)): A, B = B, A
        M,N = len(A),len(B)
        dp=[0]*(N+1)
        ans = 0
        
        for i in range(M):
            for j in range(N-1,0,-1):
                if (A[i] == B[j]):
                    dp[j + 1] = 1 + dp[j]
                else:
                    dp[j + 1] = 0
                ans=max(ans,dp[j+1])
        
        return ans
    
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        # Create a 2D DP array with dimensions (n+1)x(n+1)
        dp = [[0] * (n+1) for _ in range(n+1)]

        # Fill the DP array from bottom-up
        for i in range(n, -1, -1):
            for j in range(i+1, n+1):
                if i == j:
                    # Base case: a single character is a palindrome of length 1
                    dp[i][j] = 1
                elif s[i] == s[j-1]:
                    # If characters at i-th and j-th positions match, add 2 to the length of
                    # longest palindromic subsequence without these characters
                    dp[i][j] = 2 + dp[i+1][j-1]
                else:
                    # If characters at i-th and j-th positions don't match, take the maximum
                    # of longest palindromic subsequence without i-th character and without j-th
                    # character
                    dp[i][j] = max(dp[i+1][j], dp[i][j-1])

        return dp[0][n]
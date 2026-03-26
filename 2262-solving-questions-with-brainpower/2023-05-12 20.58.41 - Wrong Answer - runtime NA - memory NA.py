class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)
        dp = [0] * (n+1)  # dp[i] stores the maximum points you can earn if you start from question i
        
        for i in range(n-1, -1, -1):  # processing questions in reverse order
            if i + questions[i][1] >= n:  # if you can solve all the remaining questions
                dp[i] = questions[i][0]
            else:
                dp[i] = max(questions[i][0] + dp[i+questions[i][1]+1], dp[i+1])
                
        return dp[0]
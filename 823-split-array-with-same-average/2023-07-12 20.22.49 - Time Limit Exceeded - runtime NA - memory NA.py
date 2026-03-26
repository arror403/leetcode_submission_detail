class Solution:
    def splitArraySameAverage(self, nums: List[int]) -> bool:
        n = len(nums)
        total_sum = sum(nums)
        target_average = total_sum / n

        # Check for edge case where one of the arrays has only one element
        if n == 1:
            return False

        # Dynamic programming array to store possible sums for each subset size
        dp = [[False] * (total_sum + 1) for _ in range(n // 2 + 1)]
        dp[0][0] = True  # Initial condition for empty subset

        for num in nums:
            for size in range(n // 2, 0, -1):
                for curr_sum in range(total_sum, num - 1, -1):
                    if dp[size - 1][curr_sum - num]:
                        dp[size][curr_sum] = True

        for size in range(1, n // 2 + 1):
            if total_sum * size % n == 0 and dp[size][total_sum * size // n]:
                return True

        return False
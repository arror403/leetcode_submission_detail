class Solution:
    def integerBreak(self, n: int) -> int:
        if n <= 1:
            return 1

        # Base cases:

        if n == 2:
            return 1
        elif n == 3:
            return 3

        # Recursive case:

        max_product = 0
        for k in range(2, n + 1):
            max_product = max(max_product, k * self.integerBreak(n - k))

        return max_product
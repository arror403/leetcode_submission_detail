class Solution:
    def splitArraySameAverage(self, nums: List[int]) -> bool:
        total_sum = sum(nums)
        n = len(nums)

        for size_A in range(1, n // 2 + 1):
            if total_sum * size_A % n == 0 and self.partition(nums, total_sum * size_A // n, size_A, 0):
                return True

        return False

    def partition(self, nums: List[int], target_sum: int, size_A: int, idx: int) -> bool:
        if size_A == 0:
            return target_sum == 0

        if idx >= len(nums):
            return False

        if self.partition(nums, target_sum - nums[idx], size_A - 1, idx + 1):
            return True

        if self.partition(nums, target_sum, size_A, idx + 1):
            return True

        return False
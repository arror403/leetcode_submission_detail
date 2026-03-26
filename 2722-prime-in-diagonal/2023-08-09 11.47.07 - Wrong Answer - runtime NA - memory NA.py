class Solution:
    def diagonalPrime(self, nums: List[List[int]]) -> int:
        for i in range(len(nums)):
            for j in range(len(nums[0])):
                if i!=j: 
                    continue
                if self.is_prime(nums[i][j]):
                    return nums[i][j]
        return 0

    def is_prime(self, number):
        if number > 1:
            for num in range(2, int(number**0.5) + 1):
                if number % num == 0:
                    return False
            return True
        return False
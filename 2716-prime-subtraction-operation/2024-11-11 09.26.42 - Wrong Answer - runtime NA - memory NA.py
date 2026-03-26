class Solution:
    def primeSubOperation(self, nums: List[int]) -> bool:
        # Generate primes up to 1000 using sieve (only need to do once)
        primes = []
        sieve = [True] * 1001
        for i in range(2, int(1001 ** 0.5) + 1):
            if sieve[i]:
                primes.append(i)
                for j in range(i * i, 1001, i):
                    sieve[j] = False
        primes.extend([i for i in range(int(1001 ** 0.5) + 1, 1001) if sieve[i]])
        
        prev = nums[-1]
        for i in range(len(nums)-2, -1, -1):
            if nums[i] < prev:
                prev = nums[i]
                continue
                
            # Binary search for the largest prime that works
            left, right = 0, len(primes)-1
            while left <= right:
                mid = (left + right) // 2
                if primes[mid] < nums[i] and nums[i] - primes[mid] < prev:
                    prev = nums[i] - primes[mid]
                    break
                elif primes[mid] < nums[i]:
                    left = mid + 1
                else:
                    right = mid - 1
            else:
                return False
                
        return True
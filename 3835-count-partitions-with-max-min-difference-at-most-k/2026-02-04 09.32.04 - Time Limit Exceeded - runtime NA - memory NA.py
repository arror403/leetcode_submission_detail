class Solution:
    def countPartitions(self, nums: List[int], k: int) -> int:
        n = len(nums)
        MOD = 10**9 + 7

        @lru_cache(maxsize=None)
        def solve(start_index):
            # BASE CASE:
            # If we have passed the last element, we found 1 valid way to partition
            if start_index == n:
                return 1
            
            total_ways = 0
            current_min = float('inf')
            current_max = float('-inf')
            
            # Try forming a segment from start_index to i
            for i in range(start_index, n):
                # Update min and max for the current segment
                current_min = min(current_min, nums[i])
                current_max = max(current_max, nums[i])
                
                # Check the condition
                if current_max - current_min <= k:
                    # If valid, "cut" here and solve for the rest
                    ways_from_rest = solve(i + 1)
                    total_ways = (total_ways + ways_from_rest) % MOD
                else:
                    # Optimization: If the diff is > k, adding more elements
                    # will never make it <= k. We can stop this loop.
                    break
            
            return total_ways

        return solve(0)
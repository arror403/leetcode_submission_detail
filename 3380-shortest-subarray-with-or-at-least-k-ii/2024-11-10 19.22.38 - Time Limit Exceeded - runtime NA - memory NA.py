class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        """
        Find the minimum length subarray whose bitwise OR sum is at least k
        Using a simpler sliding window approach
        
        Args:
            nums: List of integers
            k: Target OR value
        
        Returns:
            Minimum length of subarray with OR sum >= k, or -1 if impossible
        """
        n = len(nums)
        left = 0
        curr_or = 0
        min_len = float('inf')
        
        for right in range(n):
            # Add the current number to OR sum
            curr_or |= nums[right]
            
            # If we found a valid window, try to minimize it
            while left <= right and curr_or >= k:
                min_len = min(min_len, right - left + 1)
                
                # Try removing the leftmost element
                # Need to recalculate OR for remaining elements
                new_or = 0
                for i in range(left + 1, right + 1):
                    new_or |= nums[i]
                
                # If removing left element still keeps OR >= k, we can shrink window
                if new_or >= k:
                    curr_or = new_or
                    left += 1
                else:
                    break
        
        return min_len if min_len != float('inf') else -1
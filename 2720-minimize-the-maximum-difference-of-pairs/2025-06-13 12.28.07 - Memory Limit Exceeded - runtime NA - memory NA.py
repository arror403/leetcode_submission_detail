class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        nums.sort()
        n = len(nums)
        
        @lru_cache(maxsize=None)
        def iHateDP(i, pairs_left):
            # Base cases
            if pairs_left == 0:
                return 0  # No more pairs needed
            if i >= n - 1:
                return float('inf')  # Can't form more pairs
            
            # Option 1: Don't take current pair, move to next element
            skip = iHateDP(i + 1, pairs_left)
            
            # Option 2: Take pair (i, i+1), move to i+2
            take = max(abs(nums[i] - nums[i + 1]), iHateDP(i + 2, pairs_left - 1))
            
            return min(skip, take)
        

        return iHateDP(0, p)


        # sys.setrecursionlimit(10000)
        # nums.sort()

        # @lru_cache(maxsize=None)
        # def iHateDP(i, x):
        #     return min(iHateDP(i+1, x), max(abs(nums[i]-nums[i+1]), iHateDP(i+2, p-1)))

        
        # return iHateDP(0, p)
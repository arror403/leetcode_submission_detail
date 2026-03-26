class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:


        ##### power by chatGPT #####


        if not nums: return []

        n = len(nums)
        if n==1: return 1

        piles = [float('inf')] * (n + 1)  # Initialize piles with infinity
        piles[0] = float('-inf')  # Set the first pile to negative infinity
        backpointers = [0] * n
        length = 0

        for i in range(n):
            low, high = 0, length
            while low <= high:
                mid = (low + high) // 2
                if piles[mid] < nums[i]:
                    low = mid + 1
                else:
                    high = mid - 1

            piles[low] = nums[i]
            backpointers[i] = piles[low - 1]
            if low > length:
                length = low

        # Reconstruct the longest increasing subsequence
        result = []
        current = piles[length]
        for i in range(length - 1, -1, -1):
            result.append(current)
            index = piles.index(current)
            current = backpointers[index]

        return len(result)
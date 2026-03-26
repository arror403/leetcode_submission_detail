class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        def maximumSubarraySum(arr):
            n = len(arr)
            maxSum = -inf

            for i in range(0, n):
                currSum = 0
                for j in range(i, n):
                    currSum = currSum + arr[j]
                    if(currSum > maxSum):
                        maxSum = currSum

            return maxSum
            
        return maximumSubarraySum(nums)
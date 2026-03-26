class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:

        ##### power by Bing #####

        def find_max_value(time_ranges):
            # Sort the time ranges by their end time
            time_ranges.sort(key=lambda x: x[1])
            
            # Initialize the DP table
            dp = [0] * (len(time_ranges) + 1)
            
            # Fill the DP table
            for i in range(1, len(time_ranges) + 1):
                # Find the first time range that does not overlap with the current time range
                j = i - 1
                while j >= 1 and time_ranges[j-1][1] > time_ranges[i-1][0]:
                    j -= 1
                
                # Update the DP table
                dp[i] = max(dp[i-1], time_ranges[i-1][2] + dp[j])
            
            return dp[-1]

        return find_max_value([list(i) for i in zip(startTime,endTime,profit)])
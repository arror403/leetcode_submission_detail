class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        groups = [[k, len(list(g))] for k, g in groupby(nums)]
        if len(groups) == groups[0][0] == 1: return len(nums) - 1
        
        max_length = 0
        cumulative_index = 0
        
        for i in range(1, len(groups)-1):
            cumulative_index += groups[i-1][1]
            
            # Check if we can delete a 0 and merge two 1 groups
            if (groups[i-1][0] == 1 and 
                groups[i][0] == 0 and 
                groups[i+1][0] == 1):
                # Calculate potential longest subarray
                current_length = groups[i-1][1] + groups[i+1][1]
                
                # Update max length if needed
                max_length = max(max_length, current_length)
        

        return max_length


        # m=[[k,len(list(g))] for k,g in groupby(nums)]
        # res=t=ind=0
        # for i in range(1,len(m)-1):
        #     ind+=m[i-1][1]
        #     if m[i-1][0]==m[i+1][0]==1 and m[i][0]==0:
        #         if (tmp:=m[i-1][1]+m[i+1][1]+1)>t:
        #             t=tmp
        #             res=ind
        # return res if res!=0 else 0
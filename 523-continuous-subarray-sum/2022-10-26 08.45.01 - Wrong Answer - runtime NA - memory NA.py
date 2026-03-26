class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        def subArraySum(arr, s):
            curr_sum = 0
            for i in range(len(arr)):
                curr_sum += arr[i]
                if curr_sum%s==0:
                    print(curr_sum,s)
                    return True
                # If curr_sum - sum already exists in map
                # we have found a subarray with target sum

                # if (curr_sum - s) in Map:
                # Map[curr_sum] = i
            return False
        if nums==[0]: return False
        for i in range(1,len(nums)):
            if nums[i-1]==nums[i]==0:
                return True
        t=[]
        for i in nums:
            if i==0: continue
            else: t.append(i)
        return subArraySum(t,k)
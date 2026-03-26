class Solution:
    ##### corrected by chatGPT #####
    def countSubarrays(self, nums: List[int], k: int) -> int:
        L=len(nums)
        res=0
        start=0
        c=Counter()

        for end in range(L):
            c[nums[end]]+=1

            while max(c.values(), default=0) >= k:
                c[nums[start]]-=1
                if c[nums[start]]==0:
                    del c[nums[start]]
                start+=1

            res+=start  # add the number of subarrays ending at 'end'

        return res
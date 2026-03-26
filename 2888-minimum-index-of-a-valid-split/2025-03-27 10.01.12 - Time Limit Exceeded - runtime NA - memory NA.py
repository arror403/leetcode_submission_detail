class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        majority = max(set(nums), key=nums.count)
        total_count = nums.count(majority)
        
        count = 0
        for i, n in enumerate(nums):
            count += n == majority
            if count * 2 > i + 1 and (total_count - count) * 2 > len(nums) - i - 1:
                return i
        return -1
        
# class Solution:
#     def minimumIndex(self, nums: List[int]) -> int:
#         n=len(nums)
#         x,f=Counter(nums).most_common(1)[0]
#         f1=1 if nums[0]==x else 0

#         for i in range(1,n):
#             if nums[i]==x: f1+=1
#             f2=f-f1
#             if ((f1/i)>0.5) and ((f2/(n-i))>0.5):
#                 return i-1


#         return -1
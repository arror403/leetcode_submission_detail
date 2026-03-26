class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        t=self.findPrefixSum(nums)
        s=sum(t)
        L=len(t)
        # print(t,s,L,nums[L:])
        if not t: return max(nums)+1

        return s if s not in nums[L:] else max(nums[L:])+1


    def findPrefixSum(self, arr):
        start = 0
        end = 1
        res = []

        while end < len(arr):
            if arr[end] == arr[end - 1] + 1:
                end += 1
            else:
                if end - start >= 2 and len(arr[start:end]) > len(res):
                    res = arr[start:end]
                start = end
                end += 1

        if end - start >= 2 and len(arr[start:end]) > len(res):
            res = arr[start:end]

        return res

    # def findPrefixSum(self, arr):
    #     start=0
    #     end=1

    #     while end<len(arr):
    #         if arr[end]==arr[end-1]+1:
    #             end+=1
    #         else:
    #             if end-start>=2:
    #                 return arr[start:end]
    #             start=end
    #             end+=1

    #     return []
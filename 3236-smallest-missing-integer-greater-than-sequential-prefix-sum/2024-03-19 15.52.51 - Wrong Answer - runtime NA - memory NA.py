class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        if len(nums)==1: return nums[0]+1

        t=self.findPrefixSum(nums)
        s=sum(t)
        L=len(t)
        
        # print(t,s,L,nums[L:])

        return s if s not in nums[L:] else max(nums[L:])+1


    def findPrefixSum(self, arr):
        start = 0
        end = 1
        longest_sequence = []

        while end < len(arr):
            if arr[end] == arr[end - 1] + 1:
                end += 1
            else:
                if end - start >= 2 and len(arr[start:end]) > len(longest_sequence):
                    longest_sequence = arr[start:end]
                start = end
                end += 1

        if end - start >= 2 and len(arr[start:end]) > len(longest_sequence):
            longest_sequence = arr[start:end]

        return longest_sequence

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
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        return self.quicksort(nums)


    def quicksort(self, arr):
        if len(arr)<=1: return arr

        pivot=arr[0]
        left=[x for x in arr[1:] if x<pivot]
        right=[x for x in arr[1:] if x>=pivot]

        return self.quicksort(left) + [pivot] + self.quicksort(right)
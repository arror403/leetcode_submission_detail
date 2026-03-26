class Solution:
    ##### power by Claude #####
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        min_val = min(min(nums1), min(nums2))
        max_val = max(max(nums1), max(nums2))

        freq1 = [0] * (max_val - min_val + 1)
        freq2 = [0] * (max_val - min_val + 1)

        for num in nums1:
            freq1[num - min_val] += 1

        for num in nums2:
            freq2[num - min_val] += 1

        for i in range(max_val - min_val + 1):
            if freq1[i] > 0 and freq2[i] > 0:
                return min_val + i

        return -1
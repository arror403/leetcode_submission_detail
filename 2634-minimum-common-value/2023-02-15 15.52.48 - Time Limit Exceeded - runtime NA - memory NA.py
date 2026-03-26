class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        nums1.sort()
        nums2.sort()
        for i in nums1:
            for j in nums2:
                if i==j:
                    return i

        return -1
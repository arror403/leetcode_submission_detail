class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        r=list(set(nums1)&set(nums2))
        return r[0] if r else -1
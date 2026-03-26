class Solution:
    ##### improved by Claude #####
    def minimumAddedInteger(self, nums1: List[int], nums2: List[int]) -> int:
        nums1.sort()
        nums2.sort()
        d = Counter(nums1)
        res = inf

        # Optimize the generation of pairs
        pairs = [(k, k) for k, f in d.items() if f >= 2]
        pairs.extend(itertools.combinations(d.keys(), 2))

        for i, j in pairs:
            R = [x for x in nums1 if x not in (i, j)]
            diff = [b - a for a, b in zip(R, nums2)]
            if len(set(diff)) == 1:
                tmp = nums2[0] - R[0]
                res = min(res, tmp)

        return res
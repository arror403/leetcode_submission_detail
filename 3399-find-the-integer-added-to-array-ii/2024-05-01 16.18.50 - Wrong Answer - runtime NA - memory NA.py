class Solution:
    def minimumAddedInteger(self, nums1: List[int], nums2: List[int]) -> int:
        d=Counter(nums1)
        res=inf
        
        m=list(itertools.combinations(d.keys(),2))
        for k,f in d.items():
            if f>=2: m.append((k,k))
        

        for i,j in m:
            R=nums1[:]
            R.remove(i)
            R.remove(j)
            tmp=min(nums2)-min(R)
            if tmp<res: res=tmp

        return res
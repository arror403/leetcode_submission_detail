class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        d = Counter(nums)
        r = []
        for v,f in d.items():
            if f<3: 
                r.append(v)
        for x in r: del d[x]

        s = {k:[] for k in d.keys()}
        if s=={}: return -1

        for i,v in enumerate(nums):
            if v in r: continue
            if len(s[v])>=3: continue
            s[v].append(i)

        # print(d, s)
        return min((t[2]-t[0])*2 for t in s.values())
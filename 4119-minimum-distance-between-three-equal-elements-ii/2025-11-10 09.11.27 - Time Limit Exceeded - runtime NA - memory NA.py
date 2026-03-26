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
            s[v].append(i)

        res = inf
        for t in s.values():
            for i in range(0, len(t)-2):
                # print(i, t[i+2], t[i])
                res = min(res, (t[i+2]-t[i])*2)

        # print(d, s)
        return res
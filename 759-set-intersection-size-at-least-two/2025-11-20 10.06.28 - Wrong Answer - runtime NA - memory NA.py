class Solution:
    def intersectionSizeTwo(self, intervals: List[List[int]]) -> int:
        d=defaultdict(int)
        s=[(a,b) for a,b in intervals]
        res=0
        used=set()

        for a,b in intervals:
            for i in range(a, b+1):
                d[i]+=1

        d=sorted(d.items(), key=lambda x:x[1])
        d2=d[:]

        L=len(intervals)
        X=set(s)
        while L and d:
            v=d.pop()[0]
            r=set()
            for t in X:
                if t[1] >= v >= t[0]:
                    used.add(v)
                    r.add(t)
                    L-=1
            if r: res+=1
            X-=r

        L=len(intervals)
        Y=set(s)
        while L and d2:
            v=d2.pop()[0]
            if v in used: continue
            r=set()
            for t in Y:
                if t[1] >= v >= t[0]:
                    r.add(t)
                    L-=1
            if r: res+=1
            Y-=r
            

        return res
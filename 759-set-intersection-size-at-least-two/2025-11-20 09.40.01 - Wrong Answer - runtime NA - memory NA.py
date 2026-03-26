class Solution:
    def intersectionSizeTwo(self, intervals: List[List[int]]) -> int:
        d=defaultdict(int)
        s=[(a,b) for a,b in intervals]
        res=0

        for a,b in intervals:
            for i in range(a, b+1):
                d[i]+=1

        d=sorted(d.items(), key=lambda x:x[1])

        L=len(intervals)
        X=set(s)
        while L:
            v=d.pop()[0]
            r=[]
            for t in X:
                if v in range(t[0],t[1]+1):
                    r.append(t)
                    L-=1
            if r: res+=1
            X-=set(r)

        L=len(intervals)
        Y=set(s)
        while L and d:
            v=d.pop()[0]
            r=[]
            for t in Y:
                if v in range(t[0],t[1]+1):
                    r.append(t)
                    L-=1
            if r: res+=1
            Y-=set(r)
            

        return res
class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        s=set([firstPerson,0])
        dt=defaultdict(set)
        t=inf

        for a,b,c in meetings:
            if a==firstPerson or b==firstPerson:
                t=min(t,c)
            dt[c].add(a)
            dt[c].add(b)

        dt=sorted(dt.items(), key=lambda x:x[0])
        
        if t==inf:
            for k,v in dt:
                if s&v: s|=v
        else:
            for k,v in dt:
                if k<t: continue
                if s&v: s|=v


        return list(s)
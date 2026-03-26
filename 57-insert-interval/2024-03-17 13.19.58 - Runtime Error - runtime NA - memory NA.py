class Solution:
    def insert(self, intervals: List[List[int]], n: List[int]) -> List[List[int]]:
        n=set(range(n[0],n[1]+1))
        t=[set(range(i[0],i[1]+1)) for i in intervals]
        res=[]

        tmp=[]
        for i,x in enumerate(t):
            if x&n:
                tmp.append(x|n)
            else:
                res.append(intervals[i])

        d=list(reduce(lambda x,y:x|y ,tmp))

        return sorted(res+[[d[0],d[-1]]], key=lambda x:x[0])
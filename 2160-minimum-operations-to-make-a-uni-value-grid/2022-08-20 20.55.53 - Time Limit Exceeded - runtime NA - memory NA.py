class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        m=reduce(lambda x,y: x+y, grid)
        m.sort()
        res=0
        tmp=m[len(m)//2]
        # print(tmp)
        # for i in range(m[len(m)//2]): res+=m[len(m)//2]-i
        for i in m:
            if (tmp-i)%x!=0: return -1
            res+=abs(tmp-i)/x
            
        return int(res)
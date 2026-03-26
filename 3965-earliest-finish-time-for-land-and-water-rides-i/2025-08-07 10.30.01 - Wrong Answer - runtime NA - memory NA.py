class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        res=inf

        for x,y in zip(landStartTime, landDuration):
            for p,q in zip(waterStartTime, waterDuration):
                if x<=p:
                    if p>(x+y):
                        res=min(res, x+p+q)
                    else:
                        res=min(res, x+y+q)
                else:
                    if x>(p+q):
                        res=min(res, p+x+y)
                    else:
                        res=min(res, p+q+y)
        

        return res
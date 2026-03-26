class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        m=sorted(zip(difficulty,profit), key=lambda x:x[0]/x[1])
        m.reverse()
        res=0
        # print(m)
        for w in worker:
            for d,p in m:
                if d<=w:
                    res+=p
                    break


        return res
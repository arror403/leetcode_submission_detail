class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        res=[]
        for i in queries:
            tmp=[]
            for j in range(i[0],i[1]+1):
                tmp.append(arr[j])
            reduce(lambda a,b : a^b,tmp)
            res.append(reduce(lambda a,b : a^b,tmp))
        return res
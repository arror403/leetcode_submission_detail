class Solution:
    def maxAbsValExpr(self, arr1: List[int], arr2: List[int]) -> int:
        res=-inf
        for i in range(len(arr1)):
            for j in range(i+1,len(arr1)):
                tmp=abs(arr1[i]-arr1[j])+abs(arr2[i]-arr2[j])+abs(i-j)
                if tmp>res: res=tmp
                    
        return res
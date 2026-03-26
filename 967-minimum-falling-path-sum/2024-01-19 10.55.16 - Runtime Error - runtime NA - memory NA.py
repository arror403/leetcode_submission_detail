class Solution:
    def minFallingPathSum(self, m: List[List[int]]) -> int:
        L=len(m)
        res=[0]*L
        for i,v in enumerate(m[0]):
            
            res[i]+=v
            
            while row<L:
                row+=1
                if (i+1)>=0 and (i-1)<=(L-1):
                    res[i]+=min(m[row][i],m[row][i+1],m[row][i-1])
                elif (i+1)<0:
                    res[i]+=min(m[row][i],m[row][i+1])
                else:
                    res[i]+=min(m[row][i],m[row][i-1])

        return min(res)
class Solution:
    def minFallingPathSum(self, m: List[List[int]]) -> int:
        L=len(m)
        res=m[0]
        for i in range(L):
            c=i
            for row in range(1,L):
                if c in range(1,L-1):
                    t=min(m[row][c],m[row][c+1],m[row][c-1])
                    res[i]+=t
                    if m[row][c+1]==t: c+=1
                    elif m[row][c-1]==t: c-=1
                elif c==0:
                    t=min(m[row][c],m[row][c+1])
                    res[i]+=t
                    if m[row][c+1]==t: c+=1 
                elif c==(L-1):
                    t=min(m[row][c],m[row][c-1])
                    res[i]+=t
                    if m[row][c-1]==t: c-=1 

        return min(res)
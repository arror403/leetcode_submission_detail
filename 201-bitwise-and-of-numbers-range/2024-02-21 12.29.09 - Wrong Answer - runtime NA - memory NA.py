class Solution:
    def rangeBitwiseAnd(self, l: int, r: int) -> int:
        n=bin(l)[2:]
        m=bin(r)[2:]
        L=len(m)
        if len(n)!=L: return 0
        if m==n: return r

        res=0

        for i in range(L):
            if m[i]!=n[i]:
                break
            else:
                res+=1

        # print(m,n,res,L)

        return int(res*'1'+(L-res)*'0',2)


        # if l==0: return 0
        # t=int(log2(l))
        # return 2**t if t==int(log2(r)) else 0
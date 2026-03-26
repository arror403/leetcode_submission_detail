class Solution:
    def minFlips(self, s: str) -> int:
        L=len(s)
        t=['1','0']
        res=inf

        for _ in range(L):
            e=o=0
            for i in range(L):
                if s[i]!=t[i%2]: e+=1
                if s[i]!=t[(i+1)%2]: o+=1
            res=min(res, e, o)
            s=s[1:]+s[0]


        return res
class Solution:
    def reorderSpaces(self, t: str) -> str:
        res=""
        l=sum(1 for i in t if i==" ")

        t=t.split()
        L=len(t)-1
        
        a,b=divmod(l,L)
        
        for x in range(L):
            res+=t[x]
            res+=" "*a

        res+=t[-1]
        res+=" "*b

        return res
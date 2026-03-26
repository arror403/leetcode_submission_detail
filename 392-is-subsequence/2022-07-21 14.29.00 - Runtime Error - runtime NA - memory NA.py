class Solution:
    def isSubsequence(self, t: str, s: str) -> bool:
        f=False
        x=0
        for i in s:
            if x<len(s) and t[x]==i:
                x+=1
            if (x+1)==len(t):
                f=True
                break
                
        return f
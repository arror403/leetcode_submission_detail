class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        return all(s[i] in t[i:] for i in range(len(s)))




        # x=0
        # if len(s)>len(t):
        #     return False
        # elif len(s) == 0:
        #     return True
        # else:
        #     for i in t:
        #         if x<len(t) and s[x]==i:
        #             x+=1
        #         if x==len(s):
        #             return True
        # return False
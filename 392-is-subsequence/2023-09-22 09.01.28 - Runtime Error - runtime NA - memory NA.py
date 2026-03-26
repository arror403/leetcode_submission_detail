class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i=0
        for e in t:
            if e==s[i]:
                i+=1
            if i==len(s)-1:
                return True

        return False
class Solution:
    def minFlips(self, s: str) -> int:
        e=o=0
        t=['1','0']

        for i in range(len(s)):
            if s[i]!=t[i%2]: e+=1
            if s[i]!=t[(i+1)%2]: o+=1


        return min(e, o)
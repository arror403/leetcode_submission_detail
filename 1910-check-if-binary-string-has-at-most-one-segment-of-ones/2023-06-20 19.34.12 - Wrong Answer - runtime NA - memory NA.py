class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        if s=='1': return True
        for i in range(len(s)-1):
            if s[i]==s[i+1] and s[i]=='1':
                return True
        return False
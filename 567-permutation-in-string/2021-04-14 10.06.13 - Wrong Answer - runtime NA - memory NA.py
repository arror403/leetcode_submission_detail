class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s=0
        for i in s1:
            for j in s2:
                if i==j:
                    s+=1
                    break
        if s==len(s1):
            return 1
        else:
            return 0
                
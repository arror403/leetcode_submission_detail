class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        n=0
        m=0
        for i in s3:
            if n<len(s1) and i==s1[n]:
                n+=1
            if m<len(s2) and i==s2[m]:
                m+=1
        # print(n,m)
        if (n+m)==len(s3) and (len(s1)+len(s2))==len(s3):
            return 1
        else:
            return 0
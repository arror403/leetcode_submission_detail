class Solution:
    def findMinimumOperations(self, s1: str, s2: str, s3: str) -> int:
        # print(s1[0],s2[0],s3[0])

        if s1[0]!=s2[0] or s2[0]!=s3[0] or s1[0]!=s3[0]: return -1

        for i in range(min(len(s1),len(s2),len(s3))):
            if s1[i]==s2[i] and s2[i]==s3[i]:
                continue
            else:
                break
        
        return len(s1)+len(s2)+len(s3)-i*3-3
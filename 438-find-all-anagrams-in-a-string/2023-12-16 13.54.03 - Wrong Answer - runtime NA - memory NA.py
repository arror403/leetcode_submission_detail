class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        p=Counter(p)
        l_s=len(s)
        l_p=len(p)

        res=[]

        for i in range(l_s):
            if Counter(s[i:i+l_p])==p:
                res.append(i)

        return res
class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        res=0
        c=-inf
        for i in words:
            if i[::-1] in words and len(dict.fromkeys(i))!=1:
                res+=len(i)
            if len(dict.fromkeys(i))==1:
                if len(i)>c:
                    c=len(i)
        return res+c if c>0 else res

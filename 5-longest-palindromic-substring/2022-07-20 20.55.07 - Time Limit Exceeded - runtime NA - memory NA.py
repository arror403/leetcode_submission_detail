class Solution:
    def longestPalindrome(self, s: str) -> str:
        m=[]
        M=0
        t=''
        res = [s[i:j] for i in range(len(s)) for j in range(i+1,len(s)+1)]
        
        for i in res:
            if self.isPalindrome(i):
                tmp=[i,len(i)]
                m.append(tmp)
        
        for i in range(len(m)):
            if m[i][1]>M:
                M=m[i][1]
                t=m[i][0]
                
        return t
        
        
    def isPalindrome(self, s):
        return 1 if s==s[::-1] else 0
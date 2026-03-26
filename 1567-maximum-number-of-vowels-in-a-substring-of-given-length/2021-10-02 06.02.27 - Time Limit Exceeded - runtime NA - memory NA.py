class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        b=[]
        tmp=0
        x=0

        for i in range(len(s)):
            if s[i]=="a" or s[i]=="i" or s[i]=="u" or s[i]=="e" or s[i]=="o":
                b.append(1)
            else:
                b.append(0)        
        
        
        while(1):
            if (k+tmp)<=len(b):
                if x < sum(b[tmp:tmp+k]):
                    x = sum(b[tmp:tmp+k])
                tmp+=1
            else:
                break
        
        return x
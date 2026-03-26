class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        p=[]
        b=[]
        q=[]
        tmp=0

        for i in range(len(s)):
            if s[i]=="a" or s[i]=="i" or s[i]=="u" or s[i]=="e" or s[i]=="o":
                b.append(1)
            else:
                b.append(0)        
        
        
        while(1):
            if (k+tmp)<=len(b):
                p.append(b[tmp:tmp+k])
                tmp+=1
            else:
                break

        for i in p:
            q.append(sum(i))
        
        
        return max(q)
            
        
        

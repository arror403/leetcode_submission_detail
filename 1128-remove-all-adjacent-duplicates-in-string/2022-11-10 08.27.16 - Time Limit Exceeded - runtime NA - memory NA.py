class Solution:
    def removeDuplicates(self, s: str) -> str:

        s=list(s)
        
        while self.util(s):
            i=0
            while i < (len(s)-1):
                if s[i]==s[i+1]:
                    del s[i]
                    del s[i]
                i+=1

        return ''.join(s)


    def util(self,x):
        for i in range(len(x)-1):
            if x[i]==x[i+1]:
                return True
        return False
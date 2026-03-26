class Solution:
    def myAtoi(self, s: str) -> int:
        t=[]
        for i in s:
            if i==' ': continue
            elif i.isnumeric() or i=='-': t.append(i)
            elif i!='-' or i!='+' or not(i.isnumeric()): break
            

        t=''.join(t)
        if len(t)==0: return 0
        t=int(t)
        if t<-2**32: return -2**32
        if t>(2**32-1): return (2**32-1)
        return t
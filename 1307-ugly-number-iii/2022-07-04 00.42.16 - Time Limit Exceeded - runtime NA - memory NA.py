class Solution:
    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:
        i=1
        g=[]

        while len(g)!=n:
            if i%a==0 or i%b==0 or i%c==0:
                g.append(i)
            i+=1
            
        return g[-1]
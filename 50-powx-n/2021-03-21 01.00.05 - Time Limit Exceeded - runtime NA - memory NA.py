class Solution:
    def myPow(self, x: float, n: int) -> float:
        tmp=1
        if n>0:
            for i in range(0,n):
                tmp*=x

            return tmp  
        elif n<0:
            for i in range(0,(-1)*n):
                tmp*=x
            tmp=1/tmp
            return tmp
            
        elif n==0:
            return tmp
class Solution:
    def reverse(self, x: int) -> int:
        if x < (-2)**31 or x > 2**31-1:
            return 0
        elif x==0:
            return 0
        else:
            if x<0:
                x=x*(-1)
                x=self.fun3(x)
                return x*(-1)   
            else:
                x=self.fun3(x)
                return x
    
    
    def fun(self, n: int) -> List[int]:
        return list(map(int,str(n)))
    
    
    def fun2(self, n: List[int]) -> List[int]:
        while n[0]==0:
            del n[0]
        return n
    
    def fun3(self, n:int) -> int:
        n=self.fun(n)
        n.reverse()
        n=self.fun2(n)
        n = [str(i) for i in n]
        n=''.join(n)
        n=int(n)
        return n
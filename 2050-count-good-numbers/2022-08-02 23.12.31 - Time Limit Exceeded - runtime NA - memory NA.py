class Solution:
    def countGoodNumbers(self, n: int) -> int:
        (a,b)=divmod(n,2)
        return (5**(a+b)*4**a)%(10**9+7)
#         return (self.Power(5,a+b)*self.Power(4,a))%(10**9+7)
    
    
#     def Power(self,a,n):
#         if(n==0):
#             return 1
#         x=self.Power(a,n/2)
#         x=x*x
#         if(n%2==1):
#             x=x*a
#         return x
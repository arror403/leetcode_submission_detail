class Solution:
    def closestDivisors(self, num: int) -> List[int]:
        a=num+2
        b=num+1
        for i in range(int(math.sqrt(a)),a+1):
            if a%i==0: 
                ra=[a//i,i]
                break
                
        for i in range(int(math.sqrt(b)),b+1):
            if b%i==0: 
                rb=[b//i,i]
                break
        
        return rb if (ra[1]-ra[0])>(rb[1]-rb[0]) else ra
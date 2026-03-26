class Solution:
    def closestDivisors(self, num: int) -> List[int]:
        a=num+2
        for i in range(int(math.sqrt(a)),a+1):
            if a%i==0:
                return [a//i,i]
            elif (a-1)%i==0: 
                return [(a-1)//i,i]
class Solution:
    def closestDivisors(self, num: int) -> List[int]:
        for i in range(int(math.sqrt(num+2)),(num+3)):
            if (num+1)%i==0: 
                return [(num+1)//i,i]
            elif (num+2)%i==0:
                return [(num+2)//i,i]

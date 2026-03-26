class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        r=[]

        while n>=3:
            r.append(n%3)
            n//=3

        r.append(n)
        

        return set(r)==set([0,1])
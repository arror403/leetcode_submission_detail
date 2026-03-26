class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        r=[]
        while n>=3:
            # print(n%3)
            if (n%3)!=1 and (n%3)!=0: return False
            n//=3

        
        return True
class Solution:
    def removeTrailingZeros(self, num: str) -> str:
        num=int(num)
        while num%10==0:
            num/=10

        return str(int(num))
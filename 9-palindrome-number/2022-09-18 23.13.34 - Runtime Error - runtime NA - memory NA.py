class Solution:
    def isPalindrome(self, x: int) -> bool:
        x=list(map(int,str(x)))
        return x==x[::-1]
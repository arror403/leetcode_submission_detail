class Solution:
    def trailingZeroes(self, n: int) -> int:
        k,res=int(math.log(n)),0
        for i in range(1,k): res+=int(n/(5**i))
        return res
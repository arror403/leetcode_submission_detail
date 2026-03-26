class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        res=''.join(sorted(map(str,nums), key=lambda x: x*10, reverse=1))

        while (res and res[0]=='0'): res=res[1:]


        return  res
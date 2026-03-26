class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        g,res=0,0
        while 1:
            g+=1
            i=0
            while (i+g)<len(nums):
                res+=nums[i+g]-nums[i]
                i+=1
            if g==(len(nums)-1): break
                
        return res
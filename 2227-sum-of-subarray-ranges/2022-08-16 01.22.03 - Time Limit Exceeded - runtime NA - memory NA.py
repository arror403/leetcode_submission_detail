class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        g,res=0,0
        while 1:
            g+=1
            i=0
            while (i+g)<len(nums):
                # print(nums[i:i+g+1])
                tmp=nums[i:i+g+1]
                res+=max(tmp)-min(tmp)
                i+=1
            if g==(len(nums)-1): break
                
        return res
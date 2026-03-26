class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        b=[]
        tmp=[]
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                for k in range(j+1,len(nums)):
                    if (nums[i]+nums[j]+nums[k])==0:
                        tmp=[nums[i],nums[j],nums[k]]
                        tmp.sort()
                        if tmp not in b:
                            b.append(tmp)
                        
                        
        return b
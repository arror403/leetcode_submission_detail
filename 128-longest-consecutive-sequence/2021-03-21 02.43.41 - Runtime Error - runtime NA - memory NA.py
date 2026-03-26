class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        b=[]
        nums.sort()
        for i in range(0,len(nums)):
            tmp=i
            sum=0
            while 1:
                if (tmp+1)<=len(nums)-1:
                    if nums[tmp]==(nums[tmp+1]-1):
                        sum+=1
                        tmp+=1
                    else: break
                else: break
            b.append(sum)
            
        return max(b)+1
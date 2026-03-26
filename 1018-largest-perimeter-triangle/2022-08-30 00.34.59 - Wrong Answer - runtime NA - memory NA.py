class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        if len(nums)==3 and self.area(nums[0],nums[1],nums[2])>0: 
            return sum(nums)
        elif len(nums)==3 and self.area(nums[0],nums[1],nums[2])==0: 
            return 0
        
        nums.sort()
        nums.reverse()
        for i in range(len(nums)-3):
            if self.area(nums[i],nums[i+1],nums[i+2]) > 0:
                return (nums[i]+nums[i+1]+nums[i+2])
        
        # print(nums)
        # print(self.area(nums[0],nums[1],nums[2]))
        
        
    def area(self, a, b, c):
        s=(a+b+c)/2
        # calculate the area
        if (s*(s-a)*(s-b)*(s-c))<0: return 0
        return (s*(s-a)*(s-b)*(s-c))**0.5
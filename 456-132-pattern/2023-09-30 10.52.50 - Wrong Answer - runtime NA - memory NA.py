class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack_32=deque()
        secondLargeNum = -inf
        
        # for (int i = nums.size() - 1; i >= 0; i--)
        for i in range(len(nums)-1,-1,-1):
            if (secondLargeNum > nums[i]):
                return True
            
            while (stack_32 and nums[i] > stack_32[-1]):
                secondLargeNum = stack_32[-1]
                stack_32.pop()

            
            stack_32.appendleft(nums[i])

        
        return False
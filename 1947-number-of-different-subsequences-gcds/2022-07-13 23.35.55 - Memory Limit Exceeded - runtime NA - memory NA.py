class Solution:
    def countDifferentSubsequenceGCDs(self, nums: List[int]) -> int:
        # print(self.AllSublists(nums))
        r=[]
        b=[]
        self.dfs(nums, [], b)
        del b[0]
        for i in b:
            if len(i)<2:
                r.append(i[0])
            else:
                r.append(self.manygcd(i))
        r=list(dict.fromkeys(r))
        # print(b)
        # print(r)
        return len(r)
    
    
    def findgcd(self, x, y):
        while(y):
            x,y = y,x%y
        return x
    

    def manygcd(self,l):
        num1=l[0]
        num2=l[1]
        gcd=self.findgcd(num1,num2)
        for i in range(2,len(l)):
            gcd=self.findgcd(gcd,l[i])
        return gcd
    
    
    def dfs(self, nums, path, ret):
        ret.append(path)
        for i in range(len(nums)):
            self.dfs(nums[i+1:], path+[nums[i]], ret)
            
            
    # Bit Manipulation    
    def subsets2(self, nums):
        res = []
        nums.sort()
        for i in xrange(1<<len(nums)):
            tmp = []
            for j in xrange(len(nums)):
                if i & 1 << j:  # if i >> j & 1:
                    tmp.append(nums[j])
            res.append(tmp)
        return res
		
        
    # Iteratively
    def subsets(self, nums):
        res = [[]]
        for num in sorted(nums):
            res += [item+[num] for item in res]
        return res
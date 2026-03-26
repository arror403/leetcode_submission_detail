class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        res=[]
        for i in queries:

            nums[i[1]]+=i[0]
            
            #print (nums)
            tmp=0
            for i in nums:
                if i%2==0:
                    tmp+=i
                
            res.append(tmp)
                
        return res
        
class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        n=len(nums)
        x,f=Counter(nums).most_common(1)[0]

        for i in range(1,n):
            f1=sum(v==x for v in nums[:i])
            f2=f-f1
            if ((f1/i)>0.5) and ((f2/(n-i))>0.5):
                return i-1


        return -1
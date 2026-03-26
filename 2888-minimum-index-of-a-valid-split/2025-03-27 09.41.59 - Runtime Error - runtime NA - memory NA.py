class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        n=len(nums)
        x,f=Counter(nums).most_common(1)[0]
        f1=0

        for i in range(n):
            if nums[i]==x:
                f1+=1
                f2=f-f1
                if (f1/(i+1)>0.5) and (f2/(n-i-1)>0.5):
                    return i


        return -1
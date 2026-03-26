class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        L=len(nums)
        R=set(x for x in range(1, L-1))
        p=q=-1

        for j in range(1, L-1):
            if nums[j]<nums[j+1]:
                continue
            else:
                p=j
                break

        for j in range(p+1, L-1):
            if nums[j]>nums[j+1]:
                continue
            else:
                q=j
                break

        if not (q+1<L and nums[q]<nums[q+1]):
            return False
        
        # print(p,q)
        return set([p,q]) <= R
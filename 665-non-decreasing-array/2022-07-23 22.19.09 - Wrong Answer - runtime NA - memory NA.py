class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        f=True
        for i in range(len(nums)-1):
            tmp=list(nums)
            if tmp[i]<=tmp[i+1]:
                continue
            else:
                tmp[i+1]=tmp[i]
                if self.nonDecreasing(tmp):
                    continue
                else:
                    f=False
                    break
                    
        return f
    
    
    def nonDecreasing(self,l):
        f=True
        for i in range(len(l)-1):
            if l[i]<=l[i+1]:
                continue
            else:
                f=False
                break
        return f   
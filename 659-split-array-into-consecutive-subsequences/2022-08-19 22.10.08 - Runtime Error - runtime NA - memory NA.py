class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        a,b=[],[]
        a.append(min(nums))
        nums.remove(min(nums))
        b.append(max(nums))
        nums.remove(max(nums))
        while len(a)<3:
            if (max(a)+1) in nums:
                tmp=(max(a)+1)
                a.append(tmp)
                nums.remove(tmp)
            else: break
                
        while len(b)<3:
            if (min(b)-1) in nums:
                tmp=(min(b)-1)
                b.insert(0,tmp)
                nums.remove(tmp)
            else: break
                
        print(a,b,nums)
        
        while 1:
            if max(nums)==min(b)-1:
                tmp=max(nums)
                b.insert(0,tmp)
                nums.remove(tmp)
            if min(nums)==max(a)+1:
                tmp=min(nums)
                a.append(tmp)
                nums.remove(tmp)
            
            if len(nums)==0: return True
            if (max(nums)!=min(b)-1 and min(nums)!=max(a)+1) or ((len(a)<3) or (len(b)<3)): return False
                
                
        print(a,b,nums)
        
        # return (len(nums)==0 and (len(a)>=3) and (len(b)>=3))
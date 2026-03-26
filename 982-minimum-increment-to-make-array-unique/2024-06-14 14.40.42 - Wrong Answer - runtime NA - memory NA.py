class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        d=sorted(chain.from_iterable([[v]*f for v,f in Counter(nums).items() if f>1]))
        t=sum(d)
        used=set()
        res=[]
        
        for v in d:
            if v not in used:
                used.add(v)
                res.append(v)
            else:
                # Find the smallest unused integer greater than the current number
                next_num=v+1
                while next_num in used: next_num+=1
                used.add(next_num)
                res.append(next_num)
        
        return sum(res)-t
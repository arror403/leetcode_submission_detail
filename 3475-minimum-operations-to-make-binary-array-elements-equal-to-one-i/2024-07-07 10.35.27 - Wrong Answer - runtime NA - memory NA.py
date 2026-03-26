class Solution:
    def minOperations(self, nums: List[int]) -> int:
        d=deque(map(bool,nums))
        res=1

        while len(d)>3:
            if not d[0]:
                d[1]=not d[1]
                d[2]=not d[2]
                res+=1
            
            d.popleft()
            # print(d)

        return res if len(set(d))==1 else -1
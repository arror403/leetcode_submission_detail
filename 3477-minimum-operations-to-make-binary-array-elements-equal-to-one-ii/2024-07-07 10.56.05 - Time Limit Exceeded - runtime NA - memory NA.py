class Solution:
    def minOperations(self, nums: List[int]) -> int:
        d=deque(map(bool,nums))
        res=0

        while len(d)>1:
            if not d[0]:
                d=deque(not x for x in d)
                res+=1

            d.popleft()


        return res if d[0] else res + 1
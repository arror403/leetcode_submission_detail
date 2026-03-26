class Solution:
    def rotateElements(self, nums: List[int], k: int) -> List[int]:
        n=[]
        p=[]
        res=[]
        for i,v in enumerate(nums):
            if v<0:
                n.append([i,v])
            else:
                p.append(v)

        L=k%len(p)
        p=deque(p[L:]+p[:L])

        n=deque(n)
        t=n.popleft()
        for x in range(len(nums)):
            if x==t[0]:
                res.append(t[1])
                if n: t=n.popleft()
            else:
                res.append(p.popleft())

        return res
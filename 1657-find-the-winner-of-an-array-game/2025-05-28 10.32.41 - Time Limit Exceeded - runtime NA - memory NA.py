class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        d=defaultdict(int)
        dq=deque(arr)

        while 1:
            if dq[0]>dq[1]:
                d[dq[0]]+=1
                if d[dq[0]]==k: return dq[0]
                tmp=dq.popleft()
                dq.rotate(-1)
                dq.appendleft(tmp)
            else:
                d[dq[1]]+=1
                if d[dq[1]]==k: return dq[1]
                dq.rotate(-1)
            # print(dq)
            # print(d)
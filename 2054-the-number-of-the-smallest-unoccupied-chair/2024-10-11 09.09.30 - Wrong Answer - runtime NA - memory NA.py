class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        f=times[targetFriend][0]
        n=0
        q=[]
        s=set()
        times.sort(key=lambda x:x[0])

        for a,b in times:
            while(q and q[-1][0]<=a):
                s.add(q[-1][1])
                heappop(q)

            if s:
                cs=s[0]
                s.remove(s[0])
            else:
                cs=n
                n+=1

            heappush(q, [b,cs])

            if f==a: return cs


        return 0
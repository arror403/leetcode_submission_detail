class Solution:
    def minChanges(self, n: int, k: int) -> int:
        if n==k: return 0

        res=0
        r=bin(n^k)[2:]
        n=bin(n)[2:]

        if len(r)<len(n): r=r.zfill(len(n))
        # print(r,n)

        for a,b in zip(r,n):
            if a==b=='1': res+=1
            elif a=='1' and b=='0': return -1
            

        return res
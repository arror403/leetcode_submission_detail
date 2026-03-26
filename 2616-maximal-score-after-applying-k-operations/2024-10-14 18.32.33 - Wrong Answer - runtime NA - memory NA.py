class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        pq=nums
        heapify(pq)
        res=0

        for i in range(k):
            x=pq[-1]
            res+=x
            if x==1:
                res+=(k-1-i)
                break

            heappop(pq)
            heappush(pq, (x+2)//3)


        return res
class Solution:
    def maximumHappinessSum(self, h: List[int], k: int) -> int:
        h.sort(reverse=True)
        t=list(accumulate(h))

        for i,v in enumerate(t[1:]):
            if v<i+1:
                return v-i*(i+1)//2


        return sum(h[:k])-(k*(k-1)//2)
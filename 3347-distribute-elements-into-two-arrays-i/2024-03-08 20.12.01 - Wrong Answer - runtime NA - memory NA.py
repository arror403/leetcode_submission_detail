class Solution:
    ##### power by Claude #####
    def resultArray(self, n: List[int]) -> List[int]:
        return [n[0], *[n[i] for i in range(2,len(n),2)]]+[n[1], *[n[i] for i in range(3,len(n),2)]]
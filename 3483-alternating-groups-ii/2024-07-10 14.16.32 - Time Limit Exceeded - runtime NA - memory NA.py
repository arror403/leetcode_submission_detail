class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        d=colors+colors[:k-1]
        return sum(1 for i in range(len(d)-k+1) if all(a!=b for a,b in pairwise(d[i:i+k])))
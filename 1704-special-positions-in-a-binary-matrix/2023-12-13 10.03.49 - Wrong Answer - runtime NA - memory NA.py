class Solution:
    def numSpecial(self, m: List[List[int]]) -> int:
        return sum([1 for i,j in zip(m,zip(*m)) if i.count(1)==j.count(1)==1])
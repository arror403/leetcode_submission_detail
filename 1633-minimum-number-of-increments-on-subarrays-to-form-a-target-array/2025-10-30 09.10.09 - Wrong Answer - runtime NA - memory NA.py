class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        m = min(target)
        t = [max(list(g)) for k,g in groupby([v-m for v in target], key=lambda x: x!=0) if k!=0]

        return sum(t) + m
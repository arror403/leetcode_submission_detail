class Solution:
    def bitwiseComplement(self, n: int) -> int:
        return n ^ ((1 << ceil(log2(n))) - 1)
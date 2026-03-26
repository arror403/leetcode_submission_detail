class Solution:
    def minOperations(self, s: str) -> int:
        return 123-min(ord(c) for c in s)
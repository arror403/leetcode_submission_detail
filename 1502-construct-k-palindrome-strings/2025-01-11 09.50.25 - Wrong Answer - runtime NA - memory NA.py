class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        if k>len(s): return False
        if k==1: return True

        d=Counter(s)
        odd_count=sum(v%2==1 for v in d.values())
        
        # The minimum number of palindromes needed is the number of odd-frequency characters
        # (each odd character must be in separate palindrome)
        # Maximum possible palindromes is the length of string
        return odd_count <= k <= len(s)
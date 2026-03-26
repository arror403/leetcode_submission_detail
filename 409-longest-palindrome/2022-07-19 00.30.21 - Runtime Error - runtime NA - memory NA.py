class Solution:
    def longestPalindrome(self, s: str) -> int:
#         res = [s[i:j] for i in range(len(s)) for j in range(i+1,len(s)+1)]
#         m=0
#         for i in res:
#             if self.isPalindrome(i) and len(i)>m:
#                 m=len(i)
#         return m

        
#     def isPalindrome(self,s):
#         return 1 if s==s[::-1] else 0
        ans = 0
        for v in collections.Counter(s).itervalues():
            ans += v / 2 * 2
            if ans % 2 == 0 and v % 2 == 1:
                ans += 1
        return ans
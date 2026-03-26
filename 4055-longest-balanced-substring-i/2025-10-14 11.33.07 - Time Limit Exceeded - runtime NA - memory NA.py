class Solution:
    def longestBalanced(self, s: str) -> int:
        k = len(s)
        L = len(s)

        while k > 1:
            for i in range(L - k + 1):
                t = Counter(s[i:i+k]).values()
                # print(t)
                if len(set(t)) == 1:
                    return sum(t)

            k -= 1


        return 1
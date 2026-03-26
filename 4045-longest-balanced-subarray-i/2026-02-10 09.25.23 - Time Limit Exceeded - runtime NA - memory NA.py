class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        L=len(nums)

        for i in range(L, -1, -1):
            for j in range(0, L-i):
                # print(nums[j:i+j+1])
                s=[set(),set()]
                for v in nums[j:i+j+1]:
                    s[v%2].add(v)

                if len(s[0])==len(s[1]): return (i+1)

        return 0
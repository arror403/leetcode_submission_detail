class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        res = inf
        n = len(cookies)
        v = [0]*k

        def solve(start, nums, v, k):
            nonlocal res

            if start==len(nums):
                M = -inf
                for i in range(k): M = max(M, v[i])
                res = min(res, M)
                return

            for i in range(k):
                v[i] += nums[start]
                solve(start+1, nums, v, k)
                v[i] -= nums[start]


        solve(0, cookies, v, k)
        

        return res
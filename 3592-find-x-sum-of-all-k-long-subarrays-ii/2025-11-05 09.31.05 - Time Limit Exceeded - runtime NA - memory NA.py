class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        d = Counter(nums[:k])
        L = len(nums)
        res = []
        # print(L)
        for i in range(L-k):
            res.append(sum(y*d[y] for y in nlargest(x, d, key=lambda x: (d[x], x))))
            d[nums[i]] -= 1
            d[nums[i+k]] += 1

        res.append(sum(y*d[y] for y in nlargest(x, d, key=lambda x: (d[x], x))))


        return res
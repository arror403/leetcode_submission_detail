class Solution:
    def countArrays(self, original: List[int], bounds: List[List[int]]) -> int:
        r = range(bounds[0][0], bounds[0][1]+1)

        for i in range(1, len(original)):
            d = original[i] - original[i-1]
            r = set(x+d for x in r) & set(range(bounds[i][0], bounds[i][1]+1))

            if not r: return 0

        # print(r)
        return len(r)
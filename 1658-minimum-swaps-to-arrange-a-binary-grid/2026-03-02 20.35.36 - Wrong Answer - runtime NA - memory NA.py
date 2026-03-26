class Solution:
    def minSwaps(self, grid: List[List[int]]) -> int:
        L=len(grid)
        s=[]
        for r in grid:
            for i in range(L-1,-1,-1):
                if r[i] and (i not in s):
                    s.append(i)
                    break

        if len(s)!=L: return -1
        # print(s)

        swaps=0
        for i in range(L-1):
            for j in range(L-1):
                if s[j] > s[j+1]:
                    s[j], s[j+1] = s[j+1], s[j]
                    swaps+=1

        return swaps
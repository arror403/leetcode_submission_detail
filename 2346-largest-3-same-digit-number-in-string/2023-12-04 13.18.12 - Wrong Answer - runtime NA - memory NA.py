class Solution:
    def largestGoodInteger(self, num: str) -> str:
        ##### improved by chatGPT #####
        return next((k*3 for k,g in groupby(num) if len(list(g))>=3), "")
class Solution:
    def stringMatching(self, w: List[str]) -> List[str]:
        return [i for i,j in combinations(sorted(dict.fromkeys(w),key=lambda x:len(x)),2) if i in j]
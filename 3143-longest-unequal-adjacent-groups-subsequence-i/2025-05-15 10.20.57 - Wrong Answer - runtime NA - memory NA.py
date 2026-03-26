class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        L = len(groups)
        if L == 1: return words
        res = []
        curr = []

        for i in range(L-1):
            if not curr: 
                curr = [words[i]]
            if groups[i] != groups[i+1]:
                curr.append(words[i+1])
            else:
                if len(curr) > 1:
                    res.append(curr)
                curr = []
        
        # Add the last subsequence if it wasn't added in the loop
        if len(curr) > 1:
            res.append(curr)
            

        return max(res, default=[], key=len)
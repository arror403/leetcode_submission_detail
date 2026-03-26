class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        res=[]
        for i in range(len(words)):
            for j in range(len(words)):
                if i!=j:
                    tmp=words[i]+words[j]
                    if tmp==tmp[::-1]: res.append([i,j])
                        
        return res
class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        t=0
        for i in words:
            while 1:
                x=0
                for j in s:
                    if x<len(i) and i[x]==j: 
                        x+=1
                if len(i)==x:
                    t+=1
                    break
                else: 
                    break
        return t
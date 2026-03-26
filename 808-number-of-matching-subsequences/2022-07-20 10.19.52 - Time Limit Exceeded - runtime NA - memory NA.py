class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        # print(self.Sub_Sequences('abcde'))
        m=self.Sub_Sequences(s)
        t=0
        for i in words:
            if i in m:
                t+=1
        return t
        

        
        
    def Sub_Sequences(self,STR):
        res=[]
        combs = []
        for l in range(1, len(STR)+1):
            combs.append(list(itertools.combinations(STR, l)))
        for c in combs:
            for t in c:
                res.append(''.join(t))
                # print (''.join(t), end =' ')
        # print(combs)
        return res
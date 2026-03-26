class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        d1,d2={},{}
        word1,word2=list(word1),list(word2)
        c1,c2=[],[]
        for i in dict.fromkeys(word1): d1[i]=0
        for i in word1: d1[i]+=1

        for i in dict.fromkeys(word2): d2[i]=0
        for i in word2: d2[i]+=1

        for k,v in d1.items():
            c1.append(v)
        for k,v in d2.items():
            c2.append(v)

        return sorted(c1)==sorted(c2)


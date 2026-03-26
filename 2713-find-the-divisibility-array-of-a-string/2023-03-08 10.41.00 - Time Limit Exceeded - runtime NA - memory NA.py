class Solution:
    def divisibilityArray(self, word: str, m: int) -> List[int]:
        word=list(word)
        word=[int(i) for i in word]
        res=[]
        for i in range(1,len(word)+1):
            tmp=word[:i]
            # print (tmp)
            tmp=int(''.join([str(i) for i in tmp]))
            if tmp%m==0:
                res.append(1)
            else:
                res.append(0)

        return res
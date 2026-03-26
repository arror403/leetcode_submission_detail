class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        res=[]
        for i in words1:
            f=True
            for j in words2:
                if j in i:
                    continue
                else:
                    f=False
                    break
                    
            if f: 
                # i=''.join(i)
                res.append(i)
                
        return res
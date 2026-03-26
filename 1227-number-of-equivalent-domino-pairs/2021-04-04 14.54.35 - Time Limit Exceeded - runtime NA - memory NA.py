class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        sum=0
        l=0
        for r in dominoes: l+=1
            
        for i in range(l):
            dominoes[i].sort()
            
        for j in range(l):
            for k in range(j+1,l):
                if dominoes[j]==dominoes[k]:
                    sum+=1
                    
        return sum
                
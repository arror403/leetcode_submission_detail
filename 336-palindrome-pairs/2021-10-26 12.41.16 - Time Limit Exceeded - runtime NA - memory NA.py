class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        b=[]
        P=[]
        t=[]
        output=[]
        for i in range(len(words)):
            for j in range(i+1,len(words)):
                b.append(''.join(words[i])+''.join(words[j]))
                t=[i,j]
                P.append(t)
                b.append(''.join(words[j])+''.join(words[i]))   
                t=[j,i]
                P.append(t)

                

        # print(P)   
        # print(b)
    
        for i in range(len(b)):
            if (self.check(b[i])==1):
                output.append(P[i])
        
        return output

        
        
    def check(self, tmp:str) -> bool:
        i=0
        j=(len(tmp)-1)
        re=1
        while(1):
            if (i==j or (j-i)==1):
                if(tmp[i]!=tmp[j]):
                    re=0
                break
            else:
                if tmp[i]==tmp[j]:
                    i+=1
                    j-=1
                elif tmp[i]!=tmp[j]:
                    re=0
                    break
        return re
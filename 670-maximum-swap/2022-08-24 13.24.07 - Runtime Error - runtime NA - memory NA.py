class Solution:
    def maximumSwap(self, num: int) -> int:
        res=[]

        num=list(map(int,str(num)))
        
        for i in range(len(num)):
            for j in range(i+1,len(num)):
                num[i],num[j]=num[j],num[i]
                res.append(int(''.join([str(x) for x in num])))
                num[i],num[j]=num[j],num[i]
                
        print(res)
                
        return max(res)
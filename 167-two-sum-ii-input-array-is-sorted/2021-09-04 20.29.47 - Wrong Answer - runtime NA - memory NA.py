class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        tmp = 0
        a=[]
        b=[]
        ai=[]
        index=0
        for i in numbers:
            index+=1
            if not i in a:
                a.append(i) 
                ai.append(index)
            
        # print (a)
        
        
        for i in range(len(a)):
            for j in range(i,len(a)):
                if (a[i]+a[j])==target and i!=j:
                    b.append(ai[i])
                    b.append(ai[j])
                    break
            # a.append(a[i])
            # if a[i] in a:
            #     if (a[i] <= target):
            #         tmp+=a[i]
            #         for j in range(i,len(a)):
            #             if tmp+a[j] == target and i != j:
            #                 b.append(ai[i])
            #                 b.append(ai[j])
            #                 break
            #     tmp=0
                        
        return b
                    
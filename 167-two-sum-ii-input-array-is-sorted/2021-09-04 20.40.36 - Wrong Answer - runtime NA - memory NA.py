class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        tmp = 0
        c=0
        b=[]
        
        a=[]
        ai=[]
        index=0
        if (target in numbers) and (0 in numbers):
            for i in range(len(numbers)):
                if numbers[i]==0:
                    b.append(i+1)
                elif numbers[i]==target:
                    b.append(i+1)
        elif target/2 in numbers:
            for i in range(len(numbers)-1):
                if(target/2==numbers[i])and(target/2==numbers[i+1]):
                    b.append(i+1)
                    b.append(i+2)
        else:
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
                        
        return b
                    
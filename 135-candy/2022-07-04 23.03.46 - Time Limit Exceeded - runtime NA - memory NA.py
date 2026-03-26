class Solution:
    def candy(self, ratings: List[int]) -> int:
        b=[]
        h=len(ratings)
        
        for i in ratings:
            b.append(1)
            
        if len(ratings)==1:
            return 1
        elif len(ratings)==2:
            if ratings[0]!=ratings[1]:
                return 3
            else:
                return 2
        
        elif len(ratings)>=3:
            while h>0:
                h-=1
                for i in range(1,len(ratings)-1):
                    if ratings[i-1] < ratings[i] and ratings[i] < ratings[i+1]:
                        while b[i-1] >= b[i]:
                            b[i]+=1
                        while b[i] >= b[i+1]:
                            b[i+1]+=1
                    elif ratings[i-1] < ratings[i] and ratings[i] > ratings[i+1]:
                        while b[i-1] >= b[i]:
                            b[i]+=1
                        while b[i] <= b[i+1]:
                            b[i]+=1
                    elif ratings[i-1] > ratings[i] and ratings[i] > ratings[i+1]:
                        while b[i-1] <= b[i]:
                            b[i-1]+=1
                        while b[i] <= b[i+1]:
                            b[i]+=1
                    elif ratings[i-1] > ratings[i] and ratings[i] < ratings[i+1]:
                        while b[i-1] <= b[i]:
                            b[i-1]+=1
                        while b[i] >= b[i+1]:
                            b[i+1]+=1
                    elif ratings[i-1] == ratings[i] and ratings[i] < ratings[i+1]:
                        while b[i] >= b[i+1]:
                            b[i+1]+=1                       
                    elif ratings[i-1] == ratings[i] and ratings[i] > ratings[i+1]:
                        while b[i] <= b[i+1]:
                            b[i]+=1        
                    elif ratings[i-1] < ratings[i] and ratings[i] == ratings[i+1]:
                        while b[i-1] >= b[i]:
                            b[i]+=1  
                    elif ratings[i-1] > ratings[i] and ratings[i] == ratings[i+1]:
                        while b[i-1] <= b[i]:
                            b[i-1]+=1
        print (b)            
        return sum(b)

class Solution:
    def candy(self, ratings: List[int]) -> int:
        b=[]
        for i in ratings:
            b.append(1)
            
        if len(ratings)>=2:
            for i in range(1,len(ratings)):
                if ratings[i]>ratings[i-1]:
                    b[i]+=1
                elif ratings[i]<ratings[i-1]:
                    b[i-1]+=1
                    
        return sum(b)
class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        b=[]
        for n in range(0,len(satisfaction)):
            index=1
            sum=0
            
            for i in satisfaction:
                sum+=index*i
                index+=1
                b.append(sum)
            
            satisfaction.remove(min(satisfaction))
            
        return max(b)
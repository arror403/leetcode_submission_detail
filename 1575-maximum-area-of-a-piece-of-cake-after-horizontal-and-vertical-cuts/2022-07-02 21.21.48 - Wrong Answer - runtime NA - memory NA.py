class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        horizontalCuts.sort()
        verticalCuts.sort()
        horizontalCuts.insert(0,0)
        horizontalCuts.append(h)
        verticalCuts.insert(0,0)
        verticalCuts.append(w)
        a=[]
        b=[]
        c=[]
        for i in range(1,len(horizontalCuts)):
            a.append(horizontalCuts[i]-horizontalCuts[i-1])
            
        for i in range(1,len(verticalCuts)):
            b.append(verticalCuts[i]-verticalCuts[i-1])
            
        for i in a:
            for j in b:
                c.append(i*j)
                
        return (max(c))
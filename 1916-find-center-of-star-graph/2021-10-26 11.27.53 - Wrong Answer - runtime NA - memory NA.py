class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        a=edges[0][0]
        b=edges[0][1]
        
        for i in range(len(edges)):
            if edges[i][0]>edges[i][1]:
                tmp=edges[i][0]
                edges[i][0]=edges[i][1]
                edges[i][1]=tmp
            
            
        if a == edges[1][0] and b != edges[1][1]:
            return a
        else:
            return b
            
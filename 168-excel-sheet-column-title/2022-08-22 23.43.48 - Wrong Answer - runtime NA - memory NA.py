class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        m,res=[],''
        while columnNumber>26:
            m.append(columnNumber%26)
            columnNumber//=26
            
        m.append(columnNumber)
        m.reverse()
        
        print(m)
        for i in m:
            if i==0: res+='Z'
            else: res+=chr(64+i)
            
        
        return res
class Solution:
    def isValid(self, intput: str) -> bool:
        s=[]
        for i in intput:
            if i=="(":
                s.append("(")
            elif i=="[":
                s.append("[")
            elif i=="{":
                s.append("{")
                
            else:
                if s==[]:
                    return 0
                    break
                elif s[-1]==i:
                    s.pop()
                else:
                    return 0
                    break
                    
        if s==[] and m==[] and l==[]:
            return 1
        else:
            return 0

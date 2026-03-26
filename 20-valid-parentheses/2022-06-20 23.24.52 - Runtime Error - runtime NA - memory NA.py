class Solution:
    def isValid(self, intput: str) -> bool:
        l=[]
        m=[]
        s=[]
        for i in intput:
            if i=="(":
                s.append("(")
            elif i=="[":
                m.append("[")
            elif i=="{":
                l.append("{")
                
            elif i==")":
                if s=="":
                    return 0
                    break
                else:
                    s.pop()
            elif i=="]":
                if m=="":
                    return 0
                    break
                else:
                    m.pop()
            elif i=="}":
                if l=="":
                    return 0
                    break
                else:
                    l.pop()
        if s==[] and m==[] and l==[]:
            return 1
        else:
            return 0

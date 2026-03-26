class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        b=self.all_perms(s1)
        # print (b)
        f=0
        for i in b:
            if (i in s2):
                f=1
                break
        return f
        
    def all_perms(self, elements : str) -> List[str]:
        x=[]
        if len(elements) <=1:
            x.append(elements)
            return x
            
        else:
            for perm in self.all_perms(elements[1:]):
                for i in range(len(elements)):
                    x.append( perm[:i] + elements[0:1] + perm[i:])
            return x
            
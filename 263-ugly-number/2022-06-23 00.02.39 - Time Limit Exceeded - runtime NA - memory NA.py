class Solution:
    def isUgly(self, n: int) -> bool:
        b=n
        a=n
        output = []
        while 1:    
            for i in range(2,(a+1)):   
                if i==b: 
                    break
                if a%i==0:
                    output.append(f'{i}')
                    a = int(a/i)
                    break
            if a==1 or a==b:
                break
        if a == b:
            output.append(str(b))

        new = list(dict.fromkeys(output))
        if n==1:
            return 1
        else:
            if (len(new)==1) and (('2' in new) or ('3' in new) or ('5' in new)):
                return 1
            elif (len(new)==2) and ((('2' in new) and ('3' in new)) or (('3' in new) and ('5' in new)) or (('2' in new) and ('5' in new))):
                return 1
            elif (len(new)==3) and (('2' in new) and ('3' in new) and ('5' in new)):
                return 1
            else:
                return 0
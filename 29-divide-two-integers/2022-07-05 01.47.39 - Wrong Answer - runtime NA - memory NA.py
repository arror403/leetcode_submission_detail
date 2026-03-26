class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        r=0
        if divisor==-1 and dividend < 0:
            r=abs(dividend)
        elif divisor==-1 and dividend > 0:
            r=-dividend
        elif divisor==1:
            r=dividend
        else:
            if dividend > 0 and divisor > 0:
                while (dividend-divisor)>=0:
                    dividend-=divisor
                    r+=1
            elif dividend < 0 and divisor < 0:
                dividend=abs(dividend)
                divisor=abs(divisor)
                while (dividend-divisor)>=0:
                    dividend-=divisor
                    r+=1            
            else:
                if dividend<0:
                    dividend=abs(dividend)
                elif divisor<0:
                    divisor=abs(divisor)

                while (dividend-divisor)>=0:
                    dividend-=divisor
                    r+=1                 
                r=abs(r)
        
        
        if r<(-2147483648):
            return -2147483648
        elif r>2147483647:
            return 2147483647
        else:    
            return r
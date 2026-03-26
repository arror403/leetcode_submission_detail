class Solution:
    def frequencySort(self, s: str) -> str:
        count=[]
        b=0
        out=[]
        for i in range(52):
            count.append(0)

        for i in s:
            if i.isupper():
                count[ord(i)-65]+=1
            elif i.islower():
                count[ord(i)-97+26]+=1

        for i in count:
            if i!=0:
                b+=1

        for i in range(b):
            tmp=count.index(max(count))
            if tmp>=26:
                for j in range(count[tmp]):
                    out.append(chr(tmp+97-26))
            else:
                for k in range(count[tmp]):
                    out.append(chr(tmp+65))
            # print(chr(tmp+97))
            count[tmp]=0

        out=''.join(out)

        return(out)
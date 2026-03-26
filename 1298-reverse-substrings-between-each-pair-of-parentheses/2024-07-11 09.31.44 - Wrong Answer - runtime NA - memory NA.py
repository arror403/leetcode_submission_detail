class Solution:
    def reverseParentheses(self, s: str) -> str:
        a,b=[],[]
        t=list(s)

        for i,c in enumerate(s):
            if c=="(": a.append(i)
            elif c==")": b.append(i)

        m=reversed(list(zip(a,reversed(b))))

        for a,b in m: t[a:b]=t[b:a:-1]


        return ''.join([x for x in t if x not in ["(",")"]])

        # For reverse a certain range of elements:
        # a[2:6] = a[2:6][::-1]
        # This also can be achieved much faster
        # a[2:6] = a[5:1:-1]
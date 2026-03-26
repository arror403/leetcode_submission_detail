class Solution:
    def squareFreeSubsets(self, nums: List[int]) -> int:
        # print(len(nums))
        def powerset(s):
            r=[]
            x=len(s)
            for i in range(1<<x): r.append([s[j] for j in range(x) if (i&(1<<j))])
            r.remove([])

            return r


        res=0

        d=Counter(nums)

        p={1:[1], 2:[2], 3:[3], 5:[5], 6:[2, 3], 7:[7], 10:[2, 5], 11:[11], 13:[13], 14:[2, 7], 15:[3, 5], 17:[17], 19:[19], 21:[3, 7], 22:[2, 11], 23:[23], 26:[2, 13], 29:[29], 30:[2, 3, 5]}

        m=set([1,2,3,5,6,7,10,11,13,14,15,17,19,21,22,23,26,29,30])

        s=list(d.keys()&m)

        for x in powerset(s):
            tmp=[]
            for i in x: tmp+=p[i]

            if len(tmp)==len(set(tmp)):
                if tmp==[1]:
                    res+=2**d[1]-1
                elif 1 in tmp:
                    res+=prod([d[v] for v in x if v!=1])*(2**d[1]-1)
                else:
                    res+=prod([d[v] for v in x])


        return res%(10**9+7)
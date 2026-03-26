class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        p=set()

        for n in map(str,arr1):
            L=len(n)
            for i in range(L):
                if (t:=n[:i+1]) not in p: p.add(t)

        p=sorted(list(p), key=lambda x:(len(x),x), reverse=True)

        print(p)

        arr2=sorted(map(str,arr2), key=lambda x:(len(x),x), reverse=True)

        for n in arr2:
            L=len(n)
            for i in range(L):
                for x in p:
                    if n[:L-i].startswith(x):
                        return len(x)

        return 0
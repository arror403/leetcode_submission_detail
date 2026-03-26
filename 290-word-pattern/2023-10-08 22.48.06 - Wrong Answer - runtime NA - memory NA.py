class Solution:
    def wordPattern(self, pattern : str, s: str) -> bool:
        if len(pattern) != len(s.split()): return False

        z=zip(pattern, s.split())

        # print(list(z))

        return all((z1[0] == z2[0]) == (z1[1] == z2[1]) for z1 in z for z2 in z)
        


        # d={}
        # for i,v in enumerate(s.split()):
        #     if pattern[i] not in d.keys():
        #         d[pattern[i]]=v
        #         # print(pattern[i],v)
        #         continue

        #     if d[pattern[i]]!=v: return False

        # if len(d.values())!=len(set(d.values())): return False

        # return True
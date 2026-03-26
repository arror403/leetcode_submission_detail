class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        d={}
        for i,v in enumerate(s.split()):
            if pattern[i] not in d.keys():
                d[pattern[i]]=v
                # print(pattern[i],v)
                continue

            if d[pattern[i]]!=v: return False

        return True
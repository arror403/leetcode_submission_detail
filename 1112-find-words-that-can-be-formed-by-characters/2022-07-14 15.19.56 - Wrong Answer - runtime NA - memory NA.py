class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        [list(i) for i in words]
        chars=list(chars)
        t=0
        for i in words:
            f=1
            for j in i:
                if j in chars:
                    continue
                else:
                    f=0
                    break
            if f:
                t+=len(i)
                
        return t
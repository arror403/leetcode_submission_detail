class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        r=""
        for c in p:
            if c not in "?*":
                r+=c
            elif c=="?":
                r+="."
            else:
                r+=".*"

        m=re.search(r, s)
        if m:
            if m.group(0)==s:
                return True

        return False
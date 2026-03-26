class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        if target not in set(letters): return letters[0]

        t=ord(target)
        for c in letters:
            if ord(c)>t:
                return c
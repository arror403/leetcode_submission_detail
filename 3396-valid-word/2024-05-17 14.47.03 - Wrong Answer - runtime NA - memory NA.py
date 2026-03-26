class Solution:
    def isValid(self, word: str) -> bool:
        return len(word)>=3 and word.isalnum() and any(c in 'aeiou' for c in word) and any(c not in 'aeiou' for c in word)
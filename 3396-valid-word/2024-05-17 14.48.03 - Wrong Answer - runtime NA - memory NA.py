class Solution:
    def isValid(self, word: str) -> bool:
        return len(word)>=3 and word.isalnum() and any(c in 'aeiouAEIOU' for c in word) and any(c not in 'aeiouAEIOU' for c in word)
class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        return set(w1) == set(w2) and Counter(Counter(w1).values()) == Counter(Counter(w2).values())


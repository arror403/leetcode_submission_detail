class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        V="aeiou"
        m=[int(((w[0] in V) and (w[-1] in V))) for w in words]

        return [sum(m[q[0]:q[1]+1]) for q in queries]
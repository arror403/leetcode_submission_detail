class Solution:
    ##### power by Gemini #####
    def customSortString(self, order: str, s: str) -> str:
        char_counts = Counter(s)  # Count characters in s efficiently
        result = []
        for char in order:
            if char in char_counts:
                result.extend(char * char_counts[char])  # Append characters directly
                del char_counts[char]  # Remove processed characters
        result.extend(char for char in char_counts)
        return ''.join(result)  # Combine characters into a string
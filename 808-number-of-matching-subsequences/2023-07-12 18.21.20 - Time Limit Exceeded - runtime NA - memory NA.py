class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        def is_subsequence(word):
            index = defaultdict(list)

            # Indexing the positions of characters in 's'
            for i, char in enumerate(s):
                index[char].append(i)

            prev_pos = -1
            for char in word:
                if char not in index or not index[char]:
                    return False

                # Perform a binary search to find the next valid position of 'char' in 's'
                positions = index[char]
                left, right = 0, len(positions) - 1
                while left <= right:
                    mid = left + (right - left) // 2
                    if positions[mid] > prev_pos:
                        right = mid - 1
                    else:
                        left = mid + 1

                if left == len(positions):
                    return False

                prev_pos = positions[left]

            return True

        count = 0
        for word in words:
            if is_subsequence(word):
                count += 1

        return count
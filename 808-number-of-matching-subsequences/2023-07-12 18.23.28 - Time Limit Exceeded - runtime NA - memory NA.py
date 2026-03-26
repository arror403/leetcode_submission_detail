class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        def is_subsequence(word):
            ptr = defaultdict(list)

            # Indexing the positions of characters in 's'
            for i, char in enumerate(s):
                ptr[char].append(i)

            prev_pos = -1
            for char in word:
                if char not in ptr or not ptr[char]:
                    return False

                positions = ptr[char]

                # Use binary search to find the next valid position of 'char' in 's'
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
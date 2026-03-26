class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        # power by chatGPT
        dq = deque(arr)
        win_count = 0
        current_winner = max(arr[0], arr[1])

        for i in range(2, len(arr)):
            if current_winner == max(dq[0], dq[1]):
                win_count += 1
            else:
                current_winner = max(dq[0], dq[1])
                win_count = 1

            dq.rotate(-1)

            if win_count == k: return current_winner

        return current_winner
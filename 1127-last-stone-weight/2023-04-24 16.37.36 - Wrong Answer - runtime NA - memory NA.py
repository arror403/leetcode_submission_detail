class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones) > 1:
            stones.sort()  # Sort the list of stones in ascending order
            x, y = stones[-2], stones[-1]  # Get the two largest stones
            if x == y:
                stones.pop(-2)  # Destroy both stones if they are equal
            else:
                stones[-2] = y - x  # Subtract the smaller stone from the larger stone
                stones.pop()  # Destroy the larger stone
        return stones[0] if stones else 0  # Return the last stone weight or 0 if the list is empty
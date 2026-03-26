class Solution:
    # assissted by perplexity
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand)%groupSize!=0: return False
        # Sort the list in ascending order
        hand.sort()
        
        # Iterate through the list with step size L
        for i in range(0, len(hand), groupSize):
            sublist = hand[i:i+groupSize]
            prev = sublist[0]
            
            # Check if the sublist contains consecutive numbers
            for num in sublist:
                if num != prev:
                    if num != prev + 1:
                        return False
                    prev = num
        
        return True
class Solution:

    ##### power by Bing #####

    def numberOfWeeks(self, milestones: List[int]) -> int:
        # Convert all frequencies into a max heap
        max_heap = [-i for i in milestones]
        heapify(max_heap)

        prev_freq = 0
        length = 0

        while max_heap:
            # Pop the most frequent object
            freq = -heappop(max_heap)
            length += 1

            # If previous object frequency is greater than zero, then push it back into the heap
            if prev_freq>0: heappush(max_heap, -prev_freq)

            # Decrease the frequency and set it as previous frequency for the next iteration
            freq-=1
            prev_freq=freq


        return length
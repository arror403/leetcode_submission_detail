class FreqStack:

    ##### power by chatGPT #####

    def __init__(self):
        self.freq_counter = defaultdict(int)
        self.grouped_elements = defaultdict(list)
        self.max_heap = []

    def push(self, x: int) -> None:
        freq = self.freq_counter[x] + 1
        self.freq_counter[x] = freq
        heapq.heappush(self.max_heap, (-freq, -len(self.grouped_elements[freq])))
        self.grouped_elements[freq].append(x)

    def pop(self) -> int:
        if self.max_heap:
            freq, index = heapq.heappop(self.max_heap)
            freq = -freq
            index = -index
            element = self.grouped_elements[freq].pop(index)
            if not self.grouped_elements[freq]:
                del self.grouped_elements[freq]
            return element
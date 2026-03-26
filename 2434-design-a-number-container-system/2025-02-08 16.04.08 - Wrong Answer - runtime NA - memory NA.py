class NumberContainers:
    def __init__(self):
        self.ind_num = {}  # index -> number
        self.num_inds = defaultdict(list)  # number -> heap of indices
        self.removed = defaultdict(set)  # Track removed indices for each number
        
    def change(self, index: int, number: int) -> None:
        # If index already has a number
        if index in self.ind_num:
            old_number = self.ind_num[index]
            if old_number != number:
                self.removed[old_number].add(index)
                self.ind_num[index] = number
                heappush(self.num_inds[number], index)
        else:
            self.ind_num[index] = number
            heappush(self.num_inds[number], index)
        
    def find(self, number: int) -> int:
        # Keep popping removed indices
        while self.num_inds[number] and self.num_inds[number][0] in self.removed[number]:
            heappop(self.num_inds[number])
            
        if self.num_inds[number]:
            return self.num_inds[number][0]  # Peek at smallest valid index
        return -1
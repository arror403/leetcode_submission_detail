class NumberContainers:
    def __init__(self):
        self.index_to_num = {}
        self.num_to_indices = defaultdict(list)
        self.invalid_indices = defaultdict(set)
        

    def change(self, index: int, number: int) -> None:
        if index in self.index_to_num:
            old_num = self.index_to_num[index]
            self.invalid_indices[old_num].add(index)
            
        self.index_to_num[index] = number
        heapq.heappush(self.num_to_indices[number], index)
        

    def find(self, number: int) -> int:
        while (self.num_to_indices[number] and 
               self.num_to_indices[number][0] in self.invalid_indices[number]):
            invalid_idx = heapq.heappop(self.num_to_indices[number])
            self.invalid_indices[number].remove(invalid_idx)
            
        if not self.num_to_indices[number]: return -1
        
        return self.num_to_indices[number][0]
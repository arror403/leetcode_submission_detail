class NumberContainers:
    def __init__(self):
        self.ind_num = defaultdict(int)
        self.num_inds = defaultdict(set)
        
    def change(self, index: int, number: int) -> None:
        if index in self.ind_num:
            old_number = self.ind_num[index]
            self.num_inds[old_number].remove(index)
            
        self.ind_num[index] = number
        self.num_inds[number].add(index)
        
    def find(self, number: int) -> int:
        if number in self.num_inds and self.num_inds[number]:
            return min(self.num_inds[number])
        return -1
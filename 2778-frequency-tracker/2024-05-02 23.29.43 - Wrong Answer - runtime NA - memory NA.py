class FrequencyTracker:

    def __init__(self):
        self.d=defaultdict(int)

    def add(self, number: int) -> None:
        self.d[number]+=1

    def deleteOne(self, number: int) -> None:
        if number in self.d.keys(): self.d[number]-=1

    def hasFrequency(self, frequency: int) -> bool:
        return frequency in self.d.values()


# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)
class FrequencyTracker:

    def __init__(self):
        self.d=Counter()

    def add(self, number: int) -> None:
        self.d[number]+=1

    def deleteOne(self, number: int) -> None:
        if self.d[number]>0: self.d[number]-=1

    def hasFrequency(self, frequency: int) -> bool:
        return frequency in self.d.values()
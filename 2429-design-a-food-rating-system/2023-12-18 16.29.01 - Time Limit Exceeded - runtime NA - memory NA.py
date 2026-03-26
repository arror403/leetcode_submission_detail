class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.m={foods[i]:cuisines[i] for i in range(len(foods))}
        self.c=defaultdict(list)
        for i in range(len(foods)): self.c[cuisines[i]].append([foods[i],ratings[i]])
        for k,v in self.c.items(): self.c[k]=sorted(v, key=lambda x: x[0])



    def changeRating(self, food: str, newRating: int) -> None: 
        for i in self.c[self.m[food]]: 
            if i[0]==food: 
                i[1]=newRating
                return



    def highestRated(self, cuisine: str) -> str:
        return max(self.c[cuisine], key=lambda x:x[1])[0]


# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)
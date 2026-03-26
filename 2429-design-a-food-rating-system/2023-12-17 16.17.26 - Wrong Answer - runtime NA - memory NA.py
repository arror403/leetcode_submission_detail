class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.f={foods[i]:[ratings[i],cuisines[i]] for i in range(len(foods))}

    def changeRating(self, food: str, newRating: int) -> None:
        if food in self.f.keys():
            self.f[food][0]=newRating

    def highestRated(self, cuisine: str) -> str:
        m=max([i[0] for i in self.f.values() if i[1]==cuisine])
        return sorted([k for k,v in self.f.items() if v[0]==m])[0]
        


# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)
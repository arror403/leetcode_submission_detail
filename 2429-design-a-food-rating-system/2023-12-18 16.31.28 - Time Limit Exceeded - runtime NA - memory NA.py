class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.food_cuisine_mapping = {foods[i]: cuisines[i] for i in range(len(foods))}
        self.cuisine_ratings = defaultdict(list)
        for food, cuisine, rating in zip(foods, cuisines, ratings):
            self.cuisine_ratings[cuisine].append((food, rating))
        for k, v in self.cuisine_ratings.items():
            self.cuisine_ratings[k] = sorted(v)

    def changeRating(self, food: str, newRating: int) -> None:
        cuisine = self.food_cuisine_mapping.get(food)
        if cuisine:
            for i, (f, r) in enumerate(self.cuisine_ratings[cuisine]):
                if f == food:
                    self.cuisine_ratings[cuisine][i] = (f, newRating)
                    break

    def highestRated(self, cuisine: str) -> str:
        return max(self.cuisine_ratings[cuisine], key=lambda x: x[1], default=("No food", 0))[0]

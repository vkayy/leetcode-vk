from typing import List
from collections import defaultdict
import heapq

class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.foodMap = defaultdict()
        self.cuisineMap = defaultdict(list)
        for i, food in enumerate(foods):
            self.foodMap[food] = (ratings[i], cuisines[i])
            heapq.heappush(self.cuisineMap[cuisines[i]], (-ratings[i], food))

    def changeRating(self, food: str, newRating: int) -> None:
        cuisine = self.foodMap[food]
        self.foodMap[food] = (newRating, cuisine)
        heapq.heappush(self.cuisineMap[cuisine], (-newRating, food))

    def highestRated(self, cuisine: str) -> str:
        cuisineFoods = self.cuisineMap[cuisine]
        while -self.foodMap[cuisineFoods[0][1]][0] != cuisineFoods[0][0]:
            heapq.heappop(cuisineFoods)
        return cuisineFoods[0][1]


# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)
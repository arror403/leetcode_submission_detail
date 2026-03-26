class FoodRatings:
    def __init__(
        self, foods: List[str], cuisines: List[str], ratings: List[int],heapify=heapify, push=heappush, pop=heappop, replace=heapreplace, exhaust=deque(maxlen=0).extendleft):
        roots = {}
        currently = {}
        heaps = defaultdict(list)

        for item, kind, rating in zip(foods, cuisines, ratings):
            heap = heaps[kind]
            roots[kind] = roots[item] = heap
            currently[item] = rating*(-1)
            rating *= (-1)
            heap.append((rating, item))

        exhaust(map(heapify, heaps.values()))
        

        def changeRating(item, rating, currently=currently, roots=roots, push=push, replace=replace):
            rating *= (-1)

            if currently[item] != rating:
                currently[item] = rating
                got, other = (roots := roots[item])[0]
                (push if currently[other] == got else replace)(roots, (rating, item))

        self.changeRating = changeRating


        def highestRated(cuisine, roots=roots, currently=currently, pop=pop):
            roots = roots[cuisine]

            while 1:
                rating, item = roots[0]
                if currently[item] == rating: return item
                pop(roots)

        self.highestRated = highestRated
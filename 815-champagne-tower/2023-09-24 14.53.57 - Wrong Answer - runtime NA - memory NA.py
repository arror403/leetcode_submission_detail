class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        if poured >= 5050: return 1

        # Initialize a 2D list to represent the glasses and their champagne levels
        res = [[0]*i for i in range(1,101)]
        res[0][0] = poured  # Pour the initial amount into the top glass

        for row in range(query_row+1):
            for col in range(row+1):
                # Calculate the overflow amount for this glass
                overflow = (res[row][col]-1) / 2 if res[row][col] > 1 else 0

                # Distribute the overflow to the glasses in the next row
                if row < 99:
                    res[row+1][col] += overflow
                    res[row+1][col+1] += overflow

        # Ensure the values are between 0 and 1
        for row in range(query_row+1):
            for col in range(row+1):
                res[row][col] = max(0, min(1, res[row][col]))

        return res[query_row][query_glass]



        # if poured>=5050: return 1

        # res=[[] for _ in range(100)]

        # for i in range(100):
        #     if poured>=(i+1):
        #         poured-=(i+1)
        #         res[i]+=[1 for _ in range(i+1)]
        #     else:
        #         res[i]+=[poured*(math.comb(i,j)/2**i) for j in range(i+1)]
        #         break

        # for i in range(100):
        #     if not res[i]: # if is empty
        #         res[i]+=[0 for _ in range(i+1)]

        # return res[query_row][query_glass]
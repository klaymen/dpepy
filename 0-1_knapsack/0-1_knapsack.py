 # dpepy - Dynamic Programming Exercises in Python
 # Exercise: 0-1 Knapsack problem

def knapsack_01(capacity, weights, values, n = -1):
    
    n = n if n >= 0 else len(weights)
    res = [[0] * (capacity+1) for i in range(n+1)]  
    
    # Go over the items and the capacities
    for item in range(n+1):
        for c in range (capacity+1):

            if item == 0 or c == 0:
                # skip the zeroth item and zero capacity
                pass

            elif weights[item-1] <= c:
                # if there is enough room left
                # check if the current(!) item has added value comparing to its weight or not
                # (Please note that the current item's index is item-1)
                res[item][c] = max(values[item-1]+res[item-1][c-weights[item-1]], res[item-1][c]) 

            else:
                # if there were no capacity for the item, then copy result from the last item's column
                res[item][c] = res[item-1][c]

    return res[n][capacity]

print(knapsack_01(20, [1,2,3,4,5,6,7,8], [8,7,6,5,4,3,2,1]))


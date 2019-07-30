 # Name: 0-1 Knapsack problem 
 # Given a set of items, each with a weight and a value, determine the number
 # of item to include in a collection so that the total weight is less
 # than or equal to a given limit and the total value is as large as possible.
 # However, an item can be included zero or one time only.
 # [wiki] (https://en.wikipedia.org/wiki/Knapsack_problem)

def knapsack_01(capacity, weights, values, n = -1):
    n = n if n >= 0 else len(weights)
    res = [[0] * (capacity+1) for i in range(n+1)]    
    
    # Go over the products
    for i in range(n+1):
        for c in range (capacity+1):
            if i == 0 or c == 0:
                res[i][c] = 0
            elif weights[i-1] <= c:
                res[i][c] = max(values[i-1]+res[i-1][c-weights[i-1]], res[i-1][c])                
            else:
                res[i][c] = res[i-1][c]    
    return res[n][capacity]

print(knapsack_01(20, [1,2,3,4,5,6,7,8], [8,7,6,5,4,3,2,1]))


  # 0-1 Knapsack problem 
 
 Given a set of items, each with a weight and a value, determine which item to include in a collection so that the total weight is less than or equal to a given limit and the total value is as large as possible. However, an item can be included zero or one time only.
 [Wiki for Knapsack problem](https://en.wikipedia.org/wiki/Knapsack_problem)
 
## Solution Idea
- Build a two-dimensional array with the dimensions item and capacity
- Calculate the values in the array above
- The given item and capacity coordinates will give the answer for the original problem
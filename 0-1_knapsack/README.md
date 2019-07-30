  # 0-1 Knapsack problem 
 
 Given a set of items, each with a weight and a value, determine which item to include in a collection so that the total weight is less than or equal to a given limit and the total value is as large as possible. However, an item can be included zero or one time only.
 Read more: [Wiki for Knapsack problem](https://en.wikipedia.org/wiki/Knapsack_problem)
 
## Dynamic Solution
- Build a two-dimensional array with the dimensions item (row) and capacity (column)
- Calculate the results in the array above column by column
- The given item and capacity coordinates will give the answer to the original problem
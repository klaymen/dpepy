# Subset Sum
 Given a list of non-negative integers, and a value sum, determine if there is a subset of the given set with sum equal to a target sum. Read more: [Wiki for Subset Sum Problem](https://en.wikipedia.org/wiki/Subset_sum_problem)
 
## Dynamic Solution
- Build a two-dimensional boolean array with the dimensions target+1 and length+1 (n+1) of the original array with default False values
- Set results for zero as True
- Check if any if the values up until the target sum is equal to the first item and then set the corresponding value in the array above to True
- Calculate the results in the array above by adding all items from the original array one by one
- The final result will be stored in the two-dimensional array for the values up until the target sum

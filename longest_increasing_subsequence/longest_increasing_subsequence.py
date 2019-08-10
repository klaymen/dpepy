 # dpepy - Dynamic Programming Exercises in Python
 # Exercise: Longest Increasing Subsequence
 # Complexity: O(n^2)

def longest_increasing_subsequence(arr):
    # Initialize the result with ones, since they are the last element of an at 
    # least 1 long subsequence.
    res = [1] * len(arr)

    # Go over the items from the second and check if they satisfy our conditions
    for i in range(1, len(arr)):
        for j in range (i):
            # Check if there the current item is greater than the previous items
            # If yes AND they yield a longer sequence, then update the results
            if arr[i] > arr [j] and res[j] + 1 > res[i]:
                res[i] = res[j] + 1
    
    # As the result array is made of the length of the 
    # Longest increasing subsequence ending with the given index
    # We only need tho return the maximum of it.
    return max(res)

print(longest_increasing_subsequence([0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]))
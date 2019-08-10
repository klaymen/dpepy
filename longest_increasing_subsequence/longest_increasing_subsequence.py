 # dpepy - Dynamic Programming Exercises in Python
 # Exercise: Longest Increasing Subsequence
 # Complexity: O(n^2)

def longest_increasing_subsequence(arr):
    res = [1] * len(arr)

    # Go over the items from the second and check if they satisfy our conditions
    for i in range(1, len(arr)):
        for j in range (i):
            # Check if there the current item is greater than the previous items
            # If yes AND they yield a longer sequence, then update the results
            if arr[i] > arr [j] and res[j] + 1 > res[i]:
                res[i] = res[j] + 1
            
    return max(res)

print(longest_increasing_subsequence([0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]))
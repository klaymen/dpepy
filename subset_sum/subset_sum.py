 # dpepy - Dynamic Programming Exercises in Python
 # Exercise: Subset sum problem
 # Complexity: O(n*target)

def subset_sum(arr, target):
    n = len(arr)
    res = [[False] * (n+1) for i in range(target+1)]  
    
    # zero is a trivial target
    for i in range(n+1):
        res[0][i] = True

    # check if the first item is equal any values below our target
    for j in range(1,target+1): 
        res[j][1] = arr[0] == j

    # incrementally extend the array and check the effect of the new item
    # then fill the result matrix in a bottom up manner for the values below the target    
    for i in range(2,n+1): 
        for j in range(1,target+1):
            # check if there might be result for the value decreased by the newly considered item (arr[i-1])
            if j < arr[i-1]:
                # if there is no result for the decreased value, then there is no change in the result ...
                res[j][i] = res[j][i-1]
            else:
                # ... otherwise we need to check if it is equal to the current value or check the corresponding earlier result 
                res[j][i] = res[j][i-1] or arr[i-1] == j or res[j-arr[i-1]][i-1]

    return res[target][n]

print(subset_sum([0, 8, 4, 12, 2, 10, 6, 14, 16, 9, 5, 13, 3, 11, 7, 15], 111))
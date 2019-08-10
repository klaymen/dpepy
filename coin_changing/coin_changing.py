# dpepy - Dynamic Programming Exercises in Python
# Exercise: Coin changing problem
# Complexity: O(n)

def coin_changing(sum, coins = [1,2,5,10,20,50,100,200]):
    result = [0] * (sum+1)    
    result[0] = 1

    # Go over coin denominations and the values up until the sum from the value of the coin
    for coin in coins:
        for val in range(coin,sum+1):                    
            # Add the number of combinations from the previous coin denominations
            result[val] += result[val-coin]        
        
    return result[-1]
 
print(coin_changing(200))


# Coin Change Problem
 
 Given a set of coin denominations, how many different ways can an amount be made using any number of coins?
 Read more: [Algorithmist on Coin Change Problem](https://www.algorithmist.com/index.php/Coin_Change)
 
## Dynamic Solution
- Build a list for the results of size of the amount plus one and set the zeroth element to 1
- Calculate the results for the given coin denominations from the bottom (collect number of combinations)
- The last item in the list will have the answer
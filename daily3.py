'''
* Difficulty: Easy
* Asked by: Facebook (Also VISA)
* Problem: Given a array of numbers representing the stock prices of a company in chronological order,
write a function that calculates the maximum profit you could have made from buying and selling that stock once.
You must buy before you can sell it.
For example, given [9, 11, 8, 5, 7, 10], you should return 5, since you could buy the stock at 5 dollars and sell it at 10 dollars.

Time Taken: 15mins
RunTime: O(n)
Space Complexity: O(1)
'''


def max_profit(price_list):
    min_price = price_list[0];
    max_difference = 0
    for i in range(1, len(price_list)):
        if price_list[i] < min_price:
            min_price = price_list[i]
        else:
            diff = price_list[i] - min_price
            if diff > max_difference:
                max_difference = diff

    return max_difference



print(max_profit([9, 11, 8, 5, 7, 10]))
print(max_profit([1, 9, 10, 5, 0, 8]))
print(max_profit([6, 7, 9, 1, 7, 2, 6, 10]))

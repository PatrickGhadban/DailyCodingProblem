'''
* Difficulty: Hard
* Asked by: Uber
* Problem: Given an array of integers, return a new array such that each element at index i of the
new array is the product of all the numbers in the original array except the one at i.
For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24].
If our input was [3, 2, 1], the expected output would be [2, 3, 6].

RunTime: O(n)
Space Complexity: O(n)
'''

def product_array(nums):
    prod_list = [0] * len(nums) #Could override the input list instead of creating a new list for a constant space complexity
    product = 1
    for num in nums:
        product *= num

    for i in range(len(nums)):
        prod_list[i] = product/nums[i]

    return prod_list

print (product_array([1, 2, 3, 4, 5]))
print (product_array([3,2,1]))
print (product_array([1,1,1,1,1,1]))
print (product_array([1,1,3,9,7,5]))

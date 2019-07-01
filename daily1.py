'''
* Difficulty: Easy
* Asked by: Google (Also Amazon)
* Problem: Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
* Bonus: Can you do this in one pass?

RunTime: O(n)
Space Complexity: O(n)
'''

def find_sum_points(nums, sum):
    s = set()
    for i in range(len(nums)):
        missing_num = sum - nums[i]
        if missing_num in s:    #Note that the time Complexity of the search function for a set is O(1) because a set is implemented as a Hash Table
            return nums[i], missing_num
        else:
            s.add(nums[i])
    return "There are no two numbers that add up to k "




print (find_sum_points([10, 15, 3, 7], 17))
print (find_sum_points([1,2,3,4,5,6,7,8,9,10], 17))
print (find_sum_points([10, 15, 3, 7], 53))
print (find_sum_points([10,5,3,4,8,2,2], 5))

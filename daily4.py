'''
* Difficulty: Easy
* Asked by: Facebook
* Problem: Given an array of integers, write a function to determine whether the array
could become non-decreasing by modifying at most 1 element.
For example, given the array [10, 5, 7], you should return true, since we can modify
the 10 into a 1 to make the array non-decreasing. Given the array [10, 5, 1], you should return false,
since we can't modify any one element to get a non-decreasing array.

Time Taken: 15mins
RunTime: O(N)
Space Complexity: O(1)

Description: Since only 1 element can be modified, if there is more than 1 case where
2 succeeding elements are decreasing, than the array can't be non-decreasing
'''

def non_decreasing(lst):
    count = 0
    for i in range(len(lst) - 1):
        if lst[i] > lst[i + 1]:
            count += 1
            if count > 1:
                return False
    return True



print (non_decreasing([10, 5, 7]))                #True
print (non_decreasing([1, 2, 3]))                 #True but not needed
print (non_decreasing([10, 2, 5, 1]))             #False
print (non_decreasing([8, 7, 5, 6, 3, 2, 1]))     #True
print (non_decreasing([8, 7, 1, 6, 3, 2]))        #True
